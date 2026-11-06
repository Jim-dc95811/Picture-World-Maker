# Technical Architecture

## Design principle

Picture World Maker separates three concerns:

1. **source raster** — the original pixels;
2. **QGIS manufacturing** — multiscale rendering into raster MBTiles;
3. **output container** — MBTiles directly or optional Compact Cache V2 / TPKX packaging.

```text
source raster
    ↓
GDAL inspection
    ↓
flat? ────────────────┐
    │                 │
    yes               no / valid georaster
    ↓                 ↓
one-time staging      preserve real CRS/geotransform
    ↓                 │
tiled working GeoTIFF │
    ↓                 │
internal overviews    │
    └───────┬─────────┘
            ↓
QGIS 3.44.9 headless worker
            ↓
native:tilesxyzmbtiles
            ↓
verified MBTiles
            ↓
optional MBTiles_to_TPKX_v0_3_0.py (mb2tpkx 1.1 structure, v0.1.5)
            ↓
verified TPKX
```

## Photo mode (v0.2.0+) - the default for flat pictures

**Why it exists.** A flat picture is parked at an exact, axis-aligned spot (see Synthetic flat-image placement): Web Mercator, 1 picture pixel = `synthetic_meters_per_pixel` map metres (default 1.0), centred on the anchor. So no reprojection is needed: every 256 x 256 tile at every zoom is just a patch of the picture, scaled. QGIS did heavy work for a crop-and-resize job and saved every tile as PNG, which made a 260 MB JPEG into a 1.77 GB TPKX in 8:46. Photo mode does the same tile set in about a minute and a quarter of the size.

**Route choice** (`PWM_PIPELINE.build`): `photo = mode == "flat" and config.photo_engine == "photo" and photo_mode_available()` (Pillow importable). Photo mode skips the QGIS Desktop check, `find_tools` and the QGIS version check, so QGIS need not be installed. Real map rasters (and `engine = qgis`) take the QGIS route unchanged.

**Inspection without QGIS.** `inspect_raster` falls back to `inspect_raster_pillow` when QGIS is missing: size from Pillow; a TIFF carrying any GeoTIFF tag (`GEOTIFF_TAGS` = 33550 ModelPixelScale, 33922 ModelTiepoint, 34264 ModelTransformation, 34735 GeoKeyDirectory) is reported as a real map raster (needs QGIS); everything else is flat. `Image.MAX_IMAGE_PIXELS = None` is set wherever giant pictures are opened (Pillow otherwise refuses anything over ~179 million pixels as a "decompression bomb").

**The tiler** (`PWM_PHOTO_TILER.build_photo_mbtiles(source, out_mbtiles, bounds, zmin, zmax, jpeg, quality, emit, cancel_event)`), bounds from `synthetic_bounds_for_config` (the same function the QGIS route uses, so the placement is identical):

1. Open the picture **once** (`load()`, RGB). Peak memory is about 5 bytes per pixel: the full picture (3 B/px) plus the reduced copies. An earlier draft kept an extra `copy()` (5.4 GB peak on a 600 Mpx photo); loading once brought it to 3.0 GB.
2. Zooms run from **finest to coarsest**. For zoom z, map metres per tile pixel `res = 156543.03392804097 / 2^z`; picture pixels per tile pixel `scale = res / mpp`. Use the largest power-of-two reduced copy with `factor <= scale` (`img.reduce(2)` chained: 2, 4, 8 ...) so Lanczos never shrinks by a huge ratio from the full picture (slow, and no better). Reduced copies smaller than the current factor are released once no coarser zoom needs them.
3. Tile range per zoom = `_tile_range(bounds, z)`; the set is exactly `estimate_synthetic_tiles` (35,216 for Kings Reach panorama 1 at Z0-18, the same as the QGIS route).
4. For tile (tx, ty): its top-left in map metres `gx0 = -20037508.342789244 + tx*256*res`, `gy0 = 20037508.342789244 - ty*256*res`; in picture pixels of the working copy `left = (gx0 - xmin)/wmpp_x`, `top = (ymax - gy0)/wmpp_y`, width/height `256*res/wmpp`. **Fractional boxes are passed straight to `resize((256,256), LANCZOS, box=(left, top, right, bottom))`** - Pillow resamples sub-pixel boxes correctly, which keeps neighbouring tiles seamless (checked: 15-tile z17 mosaic, edge within 0.5 px of the bounds).
5. Tiles fully inside the picture -> **JPEG** (quality `jpeg_quality`, default 85). Tiles on the picture's edge -> **RGBA PNG**: a transparent 256 tile with the clipped resized part pasted in, so the ocean shows around the picture. `tiles = png` makes every tile PNG.
6. Written to MBTiles as TMS rows (`(1<<z)-1-ty`), metadata format `jpg`/`png`; then the normal MBTiles verification and the TPKX converter run. The converter copies tile bytes unchanged and writes tileImageInfo **MIXED** (Esri's tile-package spec allows mixed JPEG/PNG tiles; ArcGIS Earth shows them - live-proven 2026-11-06).

**Errors and cancel.** A file Pillow cannot open raises `PhotoTilerError("Could not open this picture: ...")` -> `PictureWorldError` (plain message in the window). `MemoryError` -> a friendly "Not enough memory to open this picture in photo mode" message suggesting `engine = qgis`. `cancel_event` is checked between tiles -> `BuildCancelled`.

**Measured** (Kings Reach panorama 1, 50,000 x 12,006 px, Z0-18): 35,216 tiles (33,581 JPEG + 1,635 PNG), ~48 s here and 55 s on Jim's PC (QGIS route 8:46), TPKX 442 MB (QGIS route 1,771 MB), MBTiles 465 MB, repeat runs byte-identical.

**Config** (`Picture_World_Maker_Config.ini`, section `[PHOTO]`): `engine = photo | qgis`, `tiles = mixed | png`, `jpeg_quality = 85`.

## Raster inspection

The normal Python GUI invokes the QGIS/GDAL installation's `gdalinfo -json`. Machine-readable JSON is read from stdout separately from diagnostic stderr; the parser deliberately tolerates harmless trailing diagnostic text.

The raster is automatically classified as a real georaster only when both a usable CRS and geotransform are present.

## Synthetic flat-image placement

Synthetic placement is not claimed to be real geography.

For width `W`, height `H`, and scale `S` projected meters/source-pixel:

```text
half_width  = (W × S) / 2
half_height = (H × S) / 2
xmin = center_x - half_width
xmax = center_x + half_width
ymin = center_y - half_height
ymax = center_y + half_height
```

v0.1.3 uses a deterministic WGS84 anchor of **30°N, 80°W**, converted internally to EPSG:3857 meters. This parks flat images in the Atlantic east of Florida rather than at the 0,0 longitude/latitude intersection off Africa.

The default scale remains **1 source pixel = 1 projected meter**. This makes the maximum useful Web Mercator zoom fall around Z17, with Z18 providing slight oversampling for visual inspection.

## Why flat PNG/JPEG inputs are staged

The first automated Montreal bench run exposed a performance defect in the original approach. Leaving QGIS to make thousands of small random reads directly from a giant stream-compressed PNG kept the CPU saturated for too long.

Picture World Maker now pays the decoding cost once:

```text
large PNG/JPEG/etc.
    ↓
GDAL sequential decode
    ↓
temporary 512 × 512 tiled BigTIFF working raster
    ↓
power-of-two internal overviews
    ↓
QGIS random-access rendering
```

The staging raster is uncompressed for fast random access and deleted after success, failure, or cancellation. The original source remains untouched.

## Overview planning

Power-of-two overviews are built until the longest raster dimension has a compact whole-image overview. For the 29,684 × 7,620 Montreal test, the plan was:

```text
2, 4, 8, 16, 32, 64, 128
```

## Headless QGIS worker

The public Python 3.14.5 process does not attempt to import PyQGIS directly. Picture World Maker launches QGIS's own `python-qgis.bat`, then runs `PWM_QGIS_WORKER.py` inside the tested QGIS environment.

The worker:

1. initializes `QgsApplication` without QGIS Desktop;
2. loads the prepared raster;
3. sets the project CRS to EPSG:3857;
4. transforms real-georaster bounds when required;
5. invokes `native:tilesxyzmbtiles`;
6. emits progress/info records to the controlling GUI;
7. returns the produced MBTiles path.

Frozen rendering recipe:

- QGIS 3.44.9
- raster PNG tiles
- 96 DPI
- antialiasing ON
- metatile 4

## Heartbeat / long-operation visibility

Some QGIS/GDAL stages do not emit trustworthy incremental percentages continuously. Picture World Maker must not invent fake completion percentages.

v0.1.3 therefore adds an independent GUI heartbeat with:

- elapsed wall-clock time;
- current stage name;
- changing activity glyph;
- last meaningful worker message;
- real numeric progress only when the engine provides it.

## MBTiles verification

Before publication, Picture World Maker opens the MBTiles read-only and verifies:

- standard `tiles` columns;
- nonzero tile count;
- min/max zoom;
- raster PNG/JPEG format metadata.

## TPKX converter

Since v0.1.5 the TPKX stage is `MBTiles_to_TPKX_v0_3_0.py`, which writes the same structure as mb2tpkx 1.1 (ArcGIS Earth / ArcGIS Pro proven): Esri bundle header and missing-tile value 4, Esri published LODs, MIXED tileImageInfo, extent from the finest tiles, Windows-style stored zip entries. The earlier `MBTiles_to_TPKX_v0_1_0.py` is in Git history; see releases/v0.1.5_TEST_RELEASE_NOTES.md for the measured differences.

SHA-256 (v0.2.1; only the description line differs from the v0.1.5-v0.2.0 file):

`9fbdd81d4114cddcc99616f465d182b767cc00d26601bba142fad620d3df9dce`

`PWM_SELF_TEST.py` checks this hash and converts a probe MBTiles, then checks the bundle header, missing-tile value, tileImageInfo, LODs, iteminfo and zip entries against the ArcGIS Earth-proven structure. To compare any two TPKX files byte by byte and field by field, use `tools/tpkx_compare.py` in the ArcGIS-Earth-Unlocked repo.

The converter writes Esri Compact Cache V2 bundle files and packages them as ZIP64 TPKX. Picture World Maker verifies the TPKX ZIP, required metadata members, Compact Cache V2 storage declaration, and presence of bundle files before publication.

## Cleanup and failure behavior

- single-instance GUI guard;
- QGIS Desktop guard;
- subprocess-tree cancellation;
- temporary work under the system temp directory;
- no overwrite of an existing finished output;
- publish through a partial filename then atomic rename where practical;
- temporary staging removed after success, failure, or cancellation.
