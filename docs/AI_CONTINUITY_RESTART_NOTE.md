# Picture World Maker — AI / Maintainer Restart Note

If coming to this project cold, establish the following before changing code.

## Current truth

**2026-11-08 (Claude): 2.0 RELEASED = the 2.0 Reference** (Jim moved the whole family to 2.0 as one reference point). Program = v0.2.4 with `VERSION = "2.0"` (window 'PICTURE WORLD MAKER 2.0'); `releases/Picture_World_Maker_v2.0.zip`; older zips in `archive/`; tag `v2.0-reference`. Next feature release = 2.1.

**2026-11-06 (Claude): v0.2.4 RELEASED = WORLD SPOTS** (Jim: 'multiple places on the ocean ... each could have its own grid box'). `world_spots(config)`: 20 spots, spot 1 = the configured anchor (30 N 80 W), +1 deg east per spot along 30 N (2-10) and 31 N (11-20); `config_for_spot` = `dataclasses.replace` of the anchor; `world_spot_box_m` = the 1-degree box in Web Mercator metres (pictures are placed in Mercator metres: 1 px = 1 m Mercator, about 0.87 ground m at 30 N). Window: World spot combobox in 2. Pyramid recipe, parking line names the spot, too-big warning, `_spotNN` file suffix. Proof: KR1 spot 1 = v0.2.3 in all 30 bundles; spot 2 centre = -79.0 exactly; stand-in-Tk check of the window logic. Zip `b5b5ad4ac856ba992e413367039ab741d6e7b64e8c2b852ac1589f0358b7a3c6`.

**2026-11-06 (Claude): v0.2.3 RELEASED = QGIS REMOVED** (Jim: ArcGIS Earth opens GeoTIFFs directly). Photo mode (Pillow) is the only engine; `inspect_raster` = Pillow; every picture is built flat (`mode_suggested` always 'flat'; `has_crs` flags GeoTIFF tags for a window note); `PWM_QGIS_WORKER.py`, QGIS discovery/staging/worker code and the `[QGIS]`/QGIS-only config keys are gone; `build(raster_mode)` accepts only auto/flat. KR1 bundles byte-identical to v0.2.2. Release `archive/Picture_World_Maker_v0.2.3.zip` `8404866fb3c417663d42712b2e99081cbc12819404494f38f232c901d6b15509`. Rig `tools/test-rigs/picture_world_maker_rig.py` (ArcGIS-Earth-Unlocked) is photo-only now. Everything below about QGIS, the QGIS rig, `PWM_PROGRESS` lines etc. is history.

**2026-11-06 (Claude): v0.2.2 RELEASED = ONE OBVIOUS FILE** (Jim's packaging rule: one .bat at the top, everything else in System Files, no README / self-test .bat). `.pyw` moved into System Files (`system_files = Path(__file__).resolve().parent`); the .bat starts `System Files\START PICTURE WORLD MAKER.pyw`. Release `archive/Picture_World_Maker_v0.2.2.zip` `3197d3dad2d7e00ed8d73d36e59f848344aec90e4eb6839667c0901121c0334d`. Keep this layout in every future version.

**2026-11-06 (Claude): v0.2.1 RELEASED = NEW NAME.** Rasta Pyramid Factory -> **Picture World Maker** (Jim: 'I hate the name rasta'). Repo `Jim-dc95811/Picture-World-Maker` (Jim renames it in Settings). Files: `Picture World Maker/` folder; `PICTURE_WORLD_MAKER.py` (GUI, VERSION 'v0.2.1'), `PWM_PIPELINE.py`, `PWM_PHOTO_TILER.py`, `PWM_QGIS_WORKER.py` (PWM_PROGRESS / PWM_INFO / PWM_RESULT_JSON lines), `PWM_SELF_TEST.py`, `Picture_World_Maker_Config.ini`; `RastaError` -> `PictureWorldError`. v0.2.1 build = v0.2.0 build (0 structural differences). Release `archive/Picture_World_Maker_v0.2.1.zip` `bdab52c8658923819f6666eb4979d33ba5ef7365382440fa8ee7a7141486e7be`. Entries below keep the old names.

**2026-11-06 (Claude): v0.2.0 PHOTO MODE - LIVE-PROVEN** (Jim 00:47: 55 s, 35,216 tiles, 30 bundles): flat pictures tiled with Pillow, no QGIS; JPEG q85 inside, PNG edges, TPKX MIXED; `[PHOTO]` config section.

**2026-11-05 (Claude): v0.1.6 TEST** (branch `rasta-v0.1.6-test`) = v0.1.5 + code-review fixes: cancel message (NameError), close mid-build stops QGIS and cleans %TEMP% first, cancel via output-reader thread (`_line_pump` / `_lines_until_done`), `check_zoom_range` (TPKX <= 23), typed paths inspected. See `releases/v0.1.6_TEST_RELEASE_NOTES.md`.

**2026-11-05 (Claude): v0.1.5 TEST** replaces the TPKX stage with `MBTiles_to_TPKX_v0_3_0.py`, which writes the mb2tpkx 1.1 structure (ArcGIS Earth / Pro proven). Measured differences of the old v0.1.0 converter and the evidence are in `releases/v0.1.5_TEST_RELEASE_NOTES.md`. Branch `rasta-v0.1.5-test` until Jim's live test. Compare any two TPKX with `tools/tpkx_compare.py` in Jim-dc95811/ArcGIS-Earth-Unlocked.

## How to work on this repo (Claude, 2026-11-06)

**Read first:** `docs/TECHNICAL_ARCHITECTURE.md` (pipeline, placement, photo mode, converter), then this note's dated entries. Family-wide rules (Jim's Minimal Build Rule, full-kit test zips, page standard, credits) are in `CLAUDE.md` of Jim-dc95811/ArcGIS-Earth-Unlocked.

**Testing without Windows or QGIS** (the Claude sandbox has neither):
- `python3 "Picture World Maker/System Files/PWM_SELF_TEST.py"` (run it inside System Files; it writes `__pycache__` - delete it before zipping) - must print `PICTURE WORLD MAKER SELF TEST: PASS`. It pins the converter's SHA-256: change the converter -> update the expected hash in the self-test.
- **Pipeline rig (v0.2.3+: photo only - TPKX / Both / MBTiles / zoom-24 / cancel / GeoTIFF; `--photo` big picture):** `tools/test-rigs/picture_world_maker_rig.py` in ArcGIS-Earth-Unlocked. The pre-v0.2.3 version built a stand-in QGIS folder (shell scripts named `qgis_process.bat`, `python-qgis.bat`, `gdalinfo`, `gdal_translate`, `gdaladdo`; `command_for()` only wraps `.bat` in cmd.exe on Windows, so they run on Linux) whose "QGIS output" is any real MBTiles you pass, then runs `build()` for TPKX / Both / MBTiles / zoom-24 refusal / cancel while QGIS is silent, and photo mode with QGIS pointing nowhere. Every run must end with `temp left=0`.
- **GUI:** no Tk in the sandbox - load `PICTURE_WORLD_MAKER.py` with a stub `tkinter` module to check the title, version and message boxes (pattern in ArcGIS-Earth-Unlocked `tools/test-rigs/README.md`).
- **TPKX structure:** `tools/tpkx_compare.py` (ArcGIS-Earth-Unlocked) against a TPKX Jim has flown (`demo_lon_41.tpkx`, mb2tpkx-made) - 0 structural differences is the bar. A real-photo check: build Kings Reach panorama 1 (Jim's upload) and compare tile count (35,216 at Z0-18) and against the previous version's TPKX.
- Pillow refuses pictures over ~179 Mpx unless `Image.MAX_IMAGE_PIXELS = None` - also in your own test scripts.
- Python's `-I` flag hides the script's own folder from imports, so `python -I PWM_SELF_TEST.py` fails with "No module named PWM_PIPELINE" - not a defect; the launchers do not use `-I`.

**Releasing** (what v0.2.1 did):
1. Bump `VERSION` in `PICTURE_WORLD_MAKER.py` (there is no README text file in the package since v0.2.2 - Jim's one-obvious-file rule).
2. Copy `Picture World Maker/` to a scratch folder named `Picture_World_Maker_v<ver>`, run the self-test there, delete every `__pycache__`, zip the folder (deflate, folder at the zip root) -> `releases/Picture_World_Maker_v<ver>.zip`. Check `unzip -l` for stray files and `file *.bat` for CRLF - Python `write_text` turns CRLF into LF, so write `.bat` files as bytes.
3. SHA-256 into README; `releases/v<ver>_RELEASE_NOTES.md`; CHANGELOG; manual (`docs/USER_MANUAL.md`) + PDF via ArcGIS-Earth-Unlocked `tools/md2pdf.py` (`GH_BASE=https://github.com/Jim-dc95811/Picture-World-Maker/blob/main/ REPO_ROOT=.`, args: md, pdf, title).
4. If the zip's contents changed: update the `picture_world_maker` sheet in ArcGIS-Earth-Unlocked `tools/graphics/make_zip_sheets.py`, render (`python3 make_zip_sheets.py <outdir> picture_world_maker`) and copy to `docs/images/picture_world_maker_whats_in_the_zip(_full).png`.
5. Update the ArcGIS-Earth-Unlocked front page (download link + version) and run its `tools/linkcheck.py` and `tools/check_binaries.py`.
6. Tests go to Jim first as a full kit zip on a `<tool>-v<ver>-test` branch; main only after his live test.

**After the 2026-11-06 rename** the session git proxy needs the repo attached under its new name (`add_repo Jim-dc95811/Picture-World-Maker`, push access) - the old name's permission does not carry over (403 "not in this session's authorized repository set").

Picture World Maker is an independent **general raster-pyramid manufacturing** project.

Its core job remains converting large flat images and real georasters into verified multiscale MBTiles and, when selected, TPKX products.

### v0.1.3 TEST

Still **LIVE-PROVEN** for:

- giant flat-image automatic path;
- tiled staging and overviews;
- headless QGIS 3.44.9 manufacturing;
- verified MBTiles;
- synthetic Atlantic parking;
- long-stage heartbeat;
- London/Barcelona/Tower Bridge/Montreal workloads;
- TPKX display in ArcGIS Earth.

---

## Critical compatibility update — 2026-08-20

A downstream ArcGIS Field Maps test exposed a verified defect in the historical MBTiles -> TPKX converter lineage used by Picture World Maker v0.1.3.

Control:

```text
project converter TPKX -> Field Maps REJECTED
Esri official Usa.tpkx -> Field Maps ACCEPTED
```

This means:

- do not claim existing Picture World Maker TPKX is Field Maps-conformant;
- do not erase v0.1.3 ArcGIS Earth evidence;
- do not rewrite v0.1.3 in place;
- (2026-11-05: the converter step is done - v0.1.5 / v0.1.6 write the mb2tpkx 1.1 structure; Field Maps is still untested.)

---

## Upstream converter repair status

> **SUPERSEDED 2026-11-05:** with Jim's full edit authority the TPKX stage was replaced by `MBTiles_to_TPKX_v0_3_0.py` (the mb2tpkx 1.1 structure, proven in ArcGIS Earth) in v0.1.5 and live-proven in v0.1.6. Field Maps is still untested and still not claimed. Kept below as history.


`ESRI_CANONICAL_TPKX_TEST_v0_2_0` is **BUILT / SELF-TESTED — FIELD MAPS PENDING**.

It copies Esri's canonical Web Mercator LOD values and metadata conventions rather than recalculating them.

The next upstream gate is:

```text
small MBTiles
-> canonical v0.2.0 converter
-> small TPKX
-> physical microSD
-> Field Maps PASS
```

Do not adopt the replacement into Picture World Maker before that real target pass.

---

## After upstream PASS

> **SUPERSEDED 2026-11-05** - see the note above.


Create a new Picture World Maker test lineage that:

1. replaces only the TPKX packaging stage with the accepted canonical converter;
2. preserves the live-proven raster inspection/staging/QGIS/MBTiles core;
3. runs regression/self-tests;
4. reruns at least one known city specimen;
5. confirms ArcGIS Earth still works;
6. tests Field Maps only if Picture World Maker is going to claim that downstream compatibility.

Do not mutate or relabel the accepted v0.1.3 evidence package.

---

## v0.1.4 TEST

The TPKX / MBTiles / REST selector branch remains BUILT / SELF-TESTED history.

REST is parked and is not the current priority.

---

## Human-observed Picture World Maker results that remain valid

- London Eye deep zoom resolved individual people inside observation pods.
- Barcelona showed useful detail distributed across the city.
- Smooth pyramid levels support whole-scene -> deep-detail navigation.
- The pyramid exposes source detail; it does not invent detail.

---

## Output-size rule

Do not use source file megabytes as the primary output-size predictor.

Prioritize:

1. width x height;
2. total pixel count;
3. scene complexity;
4. source format/compression;
5. zoom range.

---

## Deployment relationship

Picture World Maker does not own Android deployment.

Current family roles:

- Picture World Maker — giant-raster pyramid manufacturing, part of the ArcGIS Earth Unlocked family (Jim-dc95811/ArcGIS-Earth-Unlocked).

---

## Do not regress

- Do not require ordinary users to operate QGIS Desktop.
- Do not random-read giant PNG/JPEG inputs through thousands of QGIS requests; preserve tiled staging + overviews.
- Do not modify source rasters.
- Do not describe synthetic placement as real geography.
- Do not rewrite v0.1.3 history to hide the downstream converter defect.
- Do not claim ArcGIS Earth acceptance proves Field Maps acceptance.
- Do not claim Field Maps compatibility until Field Maps proves it (the converter was adopted on ArcGIS Earth proof, 2026-11-05).
- Do not fake progress percentages.
- Do not make Picture World Maker dependent on any delivery system or on Field Maps.

---

## Frozen environment

> **Updated 2026-11-06:** photo mode (v0.2.0+) writes JPEG q85 + PNG-edge tiles for flat pictures and needs no QGIS; the list below is the QGIS route.


- Windows 10/11 64-bit
- Python 3.14.5
- QGIS 3.44.9
- PNG tile output
- 96 DPI
- antialiasing ON
- metatile 4

---

## Current hardening priorities

> **Status 2026-11-06:** cancellation, MBTiles-only, TPKX + MBTiles, typed-path inspection and zoom checks were done in v0.1.6 (rig-proven). Still open: a genuine georeferenced raster specimen through the QGIS route, a very large TIFF/BigTIFF, a disk-space preflight (%TEMP% on C: holds ~10 GB per gigapixel on the QGIS route), honest size reporting.


After the upstream converter gate resolves:

- cancellation during preparation/QGIS rendering;
- MBTiles-only real GUI target;
- TPKX + MBTiles combination target;
- genuine georeferenced raster specimen;
- very large TIFF/BigTIFF specimen;
- disk-space preflight;
- honest source/output size reporting.

---

## Governing principle

> **Picture World Maker manufactures the pyramid. Preserve the proven core, and inherit compatibility claims only after the real target proves them.**
