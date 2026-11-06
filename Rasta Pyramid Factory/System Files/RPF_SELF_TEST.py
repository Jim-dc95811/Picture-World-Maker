from pathlib import Path
import hashlib
from RASTA_PIPELINE import synthetic_bounds, estimate_synthetic_tiles, recommended_max_zoom, _parse_json_payload, overview_factors, web_mercator_from_lonlat, load_config, synthetic_bounds_for_config

HERE = Path(__file__).resolve().parent
errors=[]
b=synthetic_bounds(20634,10317,1.0)
if b != (-10317.0,10317.0,-5158.5,5158.5): errors.append(f"bounds mismatch: {b}")
count=estimate_synthetic_tiles(b,0,18)
if count != 12489: errors.append(f"manual-proof tile count mismatch: {count}")
if recommended_max_zoom(1.0) != 18: errors.append("recommended max zoom mismatch")

# Regression: GDAL JSON may be followed by a codec/GDAL diagnostic. v0.1.0
# concatenated streams and json.loads() raised "Extra data". The parser must
# recover the first complete JSON object without losing raster dimensions.
probe = '{"size":[29684,7620],"driverShortName":"PNG"}\nWarning 1: harmless trailing diagnostic\n'
try:
    parsed = _parse_json_payload(probe)
    if parsed.get("size") != [29684, 7620]: errors.append(f"GDAL JSON parser regression: {parsed}")
except Exception as exc:
    errors.append(f"GDAL JSON parser raised on trailing diagnostic: {exc}")

# Performance regression: giant flat rasters must be staged into a tiled GeoTIFF
# with power-of-two overviews instead of leaving QGIS to random-read a PNG/JPEG.
factors = overview_factors(29684, 7620)
if factors != [2, 4, 8, 16, 32, 64, 128]: errors.append(f"overview plan mismatch: {factors}")

# v0.1.3 regression: flat images park at a deterministic synthetic anchor
# east of Florida instead of at lon/lat 0,0 off Africa.
cfg = load_config(HERE)
cx, cy = web_mercator_from_lonlat(cfg.synthetic_anchor_lon, cfg.synthetic_anchor_lat)
if abs(cfg.synthetic_anchor_lon - (-80.0)) > 1e-9 or abs(cfg.synthetic_anchor_lat - 30.0) > 1e-9:
    errors.append(f"synthetic parking anchor mismatch: {cfg.synthetic_anchor_lon}, {cfg.synthetic_anchor_lat}")
fb = synthetic_bounds_for_config(cfg, 29684, 7620, 1.0)
if abs(((fb[0]+fb[1])/2)-cx) > 0.01 or abs(((fb[2]+fb[3])/2)-cy) > 0.01:
    errors.append(f"Florida parking center mismatch: {fb}")

conv=HERE/'MBTiles_to_TPKX_v0_3_0.py'
sha=hashlib.sha256(conv.read_bytes()).hexdigest()
expected='117904a21cfdbe9e106871b477447ccddcf68f8eace226db0af6de0c6b1f9da4'
if sha != expected: errors.append(f"converter hash mismatch: {sha}")

# v0.1.5: the converter must write the mb2tpkx 1.1 / ArcGIS-proven TPKX structure.
# Build a tiny 2-zoom PNG MBTiles, convert it, and check the parts v0.1.0 got wrong.
import json, sqlite3, struct, subprocess, sys, tempfile, zipfile, zlib, binascii
def _png256():
    def ch(k, b): return struct.pack('>I', len(b)) + k + b + struct.pack('>I', binascii.crc32(k + b) & 0xffffffff)
    raw = (b'\x00' + b'\x20\x60\xa0' * 256) * 256
    return b'\x89PNG\r\n\x1a\n' + ch(b'IHDR', struct.pack('>IIBBBBB', 256, 256, 8, 2, 0, 0, 0)) + ch(b'IDAT', zlib.compress(raw)) + ch(b'IEND', b'')
with tempfile.TemporaryDirectory() as td:
    mbt = Path(td) / 'probe.mbtiles'; out = Path(td) / 'probe.tpkx'
    con = sqlite3.connect(mbt)
    con.execute('CREATE TABLE metadata (name text, value text)')
    con.execute('CREATE TABLE tiles (zoom_level integer, tile_column integer, tile_row integer, tile_data blob)')
    con.executemany('INSERT INTO metadata VALUES (?,?)', [('name', 'probe'), ('format', 'png')])
    t = _png256()
    con.executemany('INSERT INTO tiles VALUES (?,?,?,?)', [(1, 0, 1, t), (1, 1, 1, t), (2, 1, 2, t)])
    con.commit(); con.close()
    r = subprocess.run([sys.executable, str(conv), str(mbt), str(out)], capture_output=True, text=True)
    if r.returncode != 0 or not out.is_file():
        errors.append('converter failed on probe: ' + (r.stdout + r.stderr)[-300:])
    else:
        with zipfile.ZipFile(out) as z:
            names = [i.filename for i in z.infolist()]
            if names[:3] != ['iteminfo.json', 'root.json', 'thumbnail.png']: errors.append(f'member order: {names[:3]}')
            if any(i.compress_type != zipfile.ZIP_STORED or i.create_system != 0 for i in z.infolist()): errors.append('zip entries not stored/Windows-style')
            root = json.loads(z.read('root.json')); item = json.loads(z.read('iteminfo.json'))
            if root['tileImageInfo'] != {'format': 'MIXED', 'compressionQuality': 75, 'bandCount': 1, 'lercError': 0}: errors.append(f"tileImageInfo: {root['tileImageInfo']}")
            if root['tileInfo']['lods'][0] != {'level': 0, 'resolution': 156543.033928, 'scale': 591657527.591555}: errors.append('LOD 0 is not the Esri published value')
            if (root['minLOD'], root['maxLOD'], root['storageInfo']['packetSize']) != (1, 2, 128): errors.append('LOD range / packet size wrong')
            if item['tags'] != '' or item['creator'] != 'MBTilesDirectConverter': errors.append('iteminfo tags/creator wrong')
            bun = z.read('tile/L01/R0000C0000.bundle')
            hdr = struct.unpack_from('<4I3Q6I', bun, 0)
            if hdr[:2] != (3, 0) or hdr[2] != 131092 or hdr[3] != 5 or hdr[5] != len(bun) or hdr[6:] != (40, 131092, 3, 0, 16384, 5, 131072):
                errors.append(f'bundle header differs from the ArcGIS-proven reference: {hdr}')
            idx = struct.unpack_from('<16384Q', bun, 64)
            if sum(1 for v in idx if v != 4) != 2 or idx[2] != 4: errors.append('missing-tile index value must be 4 (Esri)')
            if bun[(idx[0] & ((1 << 40) - 1)):][:8] != t[:8]: errors.append('tile bytes not copied unchanged')
if errors:
    print('RASTA SELF TEST: FAIL')
    for e in errors: print(' -',e)
    raise SystemExit(1)
print('RASTA SELF TEST: PASS')
print('Manual proof synthetic bounds:', b)
print('Manual proof Z0-Z18 tile addresses:', f'{count:,}')
print('1 m/pixel recommended max zoom:', recommended_max_zoom(1.0))
print('29,684 px working overview factors:', factors)
print('Synthetic parking anchor:', f'{cfg.synthetic_anchor_lat:.1f}N {abs(cfg.synthetic_anchor_lon):.1f}W')
print('TPKX converter MBTiles_to_TPKX_v0_3_0.py (mb2tpkx 1.1 structure) SHA-256:', sha)
