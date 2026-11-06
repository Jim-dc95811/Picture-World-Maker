# Rasta Pyramid Factory Changelog

## v0.2.0 TEST — 2026-11-06 — PHOTO MODE, BUILT / SELF-TESTED

- Flat pictures are tiled directly with Pillow (`RPF_PHOTO_TILER.py`) - no QGIS needed for photos. Same tile set and placement as the QGIS route.
- JPEG tiles inside the picture, PNG with transparency on its edges (TPKX MIXED). Kings Reach panorama 1: TPKX 442 MB (v0.1.6: 1,771 MB), about 48 s (v0.1.6: 8:46).
- Real map rasters keep the QGIS route; without QGIS, pictures are inspected with Pillow and GeoTIFF coordinate tags are recognised.
- `[PHOTO]` settings in `Rasta_Config.ini` (engine, tiles, jpeg_quality); launchers install Pillow automatically.
- Details: [releases/v0.2.0_TEST_RELEASE_NOTES.md](releases/v0.2.0_TEST_RELEASE_NOTES.md).

## v0.1.6 — 2026-11-05 — LIVE-PROVEN, released

Jim's live build: Kings Reach panorama 1 (50,000 x 12,006 px, 35,216 tiles, 8:46) -> TPKX -> ArcGIS Earth: PASS. Download: `releases/Rasta_Pyramid_Factory_v0.1.6.zip`. New user manual (`docs/USER_MANUAL.md` + PDF) and 'What's in the zip' sheet.


Full code review of Rasta (pipeline, window, QGIS worker, launchers). Fixes, each confirmed by a test before and after:

- **Cancelled message never appeared.** The message box referred to the error after Python had already deleted it (NameError in a background callback, invisible without a console). Now bound at once - the box shows.
- **Closing the window mid-build left QGIS running.** The window closed at once, which ended the build thread before it could stop QGIS/GDAL, so they kept running hidden and the temporary working folder (gigabytes on big jobs) stayed behind. Now Close stops the build, waits for the clean-up, then closes.
- **Cancel waited for QGIS to speak.** Output is now read on a helper thread, so Cancel stops the job within about a second even when QGIS prints nothing for a long time (test: 1.0 s, v0.1.5: 60 s).
- **Max zoom 24-25 with TPKX failed only at the very end.** TPKX (Esri's tiling scheme) stops at zoom 23; v0.1.5's converter refuses higher, but only after QGIS had rendered everything. Now checked before any work starts (MBTiles-only may still use 24-25).
- **A path typed or pasted into the image box** (or changed after CHOOSE IMAGE) is now inspected before building; the tile estimate also updates when the zooms change.
- Self-test adds the zoom rule. Pipeline rig with stand-in QGIS/GDAL: TPKX, Both and MBTiles builds pass and clean up; TPKX through the full pipeline = Jim's flown London TPKX (0 structural differences).
- Release notes: [releases/v0.1.6_TEST_RELEASE_NOTES.md](releases/v0.1.6_TEST_RELEASE_NOTES.md).

## v0.1.5 TEST — 2026-11-05 — BUILT / SELF-TESTED

- New TPKX stage: `MBTiles_to_TPKX_v0_3_0.py` writes the same TPKX structure as mb2tpkx 1.1 (proven in ArcGIS Earth and ArcGIS Pro). Checked layer by layer against Jim's flown London TPKX: 0 structural differences, bundles byte-identical.
- Fixed versus v0.1.0: bundle header fields, missing-tile index value (4), tileImageInfo, Esri LOD values, extent from the finest tiles, iteminfo fields, zip entry style, thumbnail.
- Self-test now converts a probe MBTiles and checks the structure; `MBTiles_to_TPKX_v0_1_0.py` retired (in Git history).
- Everything before the TPKX stage is the v0.1.3 LIVE-PROVEN baseline, unchanged. Details: [releases/v0.1.5_TEST_RELEASE_NOTES.md](releases/v0.1.5_TEST_RELEASE_NOTES.md).

## 2026-08-20 — TPKX Field Maps compatibility boundary added

A downstream ArcGIS Field Maps control test found a verified compatibility defect in the historical MBTiles -> TPKX converter lineage inherited by Rasta.

- project converter-built TPKX: **Field Maps REJECTED**;
- Esri official `Usa.tpkx`: **Field Maps ACCEPTED** through the same physical-card/Designer workflow.

This does **not** invalidate Rasta v0.1.3's live-proven giant-raster manufacturing or ArcGIS Earth acceptance.

Status correction:

- Rasta v0.1.3 giant-raster core: **LIVE-PROVEN**;
- historical Rasta TPKX -> ArcGIS Earth: **LIVE-PROVEN**;
- historical Rasta TPKX -> Field Maps: **NOT APPROVED / converter repair required**;
- Esri-canonical converter replacement: **upstream BUILT / SELF-TESTED, Field Maps pending**.

The accepted v0.1.3 evidence is preserved unchanged. A corrected TPKX stage was to follow in a new Rasta test line - done in v0.1.5 / v0.1.6 (mb2tpkx 1.1 structure).

---

## 2026-08-18 — deployment separation clarified

- Kept **v0.1.3 TEST** as the current LIVE-PROVEN Rasta baseline.
- Kept **v0.1.4 TEST** as BUILT / SELF-TESTED until real target acceptance.
- Marked the shared-storage / network delivery experiment as parked.
- Clarified that Rasta manufactures pyramids and does not own router/mobile delivery architecture.

## v0.1.4 TEST — 2026-08-17 — BUILT / SELF-TESTED

- Built from the v0.1.3 LIVE-PROVEN baseline.
- Added independent TPKX / MBTiles / REST output selectors.
- QGIS renders MBTiles once; TPKX and REST branch from that verified MBTiles.
- Added Static REST WMTS conversion experiment.
- v0.1.3 remains the live-proven baseline.
- REST is now parked.

---

## 2026-08-16 — gigapixel / deep-navigation acceptance expansion

### Tower Bridge

- 15,287 x 7,643 JPEG;
- 6,976 tiles;
- Z0-Z18;
- 22 bundles;
- 0:02:18;
- Windows File Explorer TPKX size 294,910 KB;
- ArcGIS Earth PASS.

### Kings Reach Panorama 2

- 63,000 x 18,589 JPEG;
- approximately 1.17 billion source pixels;
- 67,619 tiles;
- Z0-Z18;
- 30 bundles;
- 0:23:07;
- Windows File Explorer TPKX size 1,949,149 KB;
- ArcGIS Earth PASS;
- deep navigation resolved people inside London Eye observation pods.

### Tibidabo / Barcelona

- 62,141 x 14,606 JPEG;
- approximately 908 million source pixels;
- 52,482 tiles;
- Z0-Z18;
- 30 bundles;
- 0:20:40;
- ArcGIS Earth PASS.

### Lessons

- source file megabytes do not predict pyramid size;
- pixel dimensions/total pixels matter more;
- long-stage heartbeat/status behavior is live-proven;
- dense daylight cityscapes are strong demonstrations.

## v0.1.3 TEST — 2026-08-16

- LIVE-PROVEN automatic flat-image path and ArcGIS Earth output.
- Montreal automated run: 29,684 x 7,620, 13,381 tiles, 52 bundles, 0:05:04, ArcGIS Earth PASS.
- Deterministic Atlantic synthetic placement near 30°N / 80°W.
- Independent heartbeat with elapsed time and stage labels.

## v0.1.2 TEST — 2026-08-16

- Added tiled GeoTIFF staging and power-of-two overviews for giant flat images.
- Removed normal GUI manual flat/geo mode selection.

## v0.1.1 TEST — 2026-08-16

- Hardened `gdalinfo -json` parsing against diagnostic/trailing output.

## v0.1.0 TEST — 2026-08-16

- Created Rasta Pyramid Factory.
- Added automatic inspection, synthetic EPSG:3857 placement, headless QGIS MBTiles manufacturing, MBTiles / TPKX / Both outputs, verification, cleanup, and self-test.
- Preserved the historical `MBTiles_to_TPKX_v0_1_0.py` converter lineage then in use.
