PICTURE WORLD MAKER v0.2.1
(formerly Rasta Pyramid Factory)
SLICE - DICE - PRESENT

PURPOSE
Picture World Maker turns giant raster imagery into smooth multiscale raster tile pyramids without requiring the operator to run QGIS Desktop manually.

CURRENT STATUS
- Manual arbitrary-raster pipeline: LIVE-PROVEN.
- Picture World Maker v0.1.2 automated Montreal skyline pipeline: LIVE-PROVEN.
- Picture World Maker v0.1.3 automatic flat-image manufacture + Florida/Atlantic synthetic parking + verified TPKX publication + ArcGIS Earth display: LIVE-PROVEN.
- Picture World Maker v0.1.6 (TPKX step = mb2tpkx 1.1 structure, plus five fixes): LIVE-PROVEN 2026-11-05 - Kings Reach panorama 1 (50,000 x 12,006 px, 35,216 tiles, 8:46) built and flown in ArcGIS Earth.
- Picture World Maker v0.2.0 photo mode (no QGIS for pictures): LIVE-PROVEN 2026-11-06 - the same panorama in 55 s, 35,216 tiles, TPKX 442 MB.
- v0.2.1 = v0.2.0 with the new name (Rasta Pyramid Factory -> Picture World Maker); builds are identical.

REQUIREMENTS
- Windows 10/11 64-bit
- Python 3.14.5 64-bit
- QGIS 3.44.9 at the normal configured path - only for real map rasters (GeoTIFFs with coordinates) since v0.2.0

NORMAL OPERATOR WORKFLOW
1. Run "Run Picture World Maker Self Test.bat" once after extraction.
   (User manual: https://github.com/Jim-dc95811/Picture-World-Maker/blob/main/docs/USER_MANUAL.md)
2. Launch "Start Picture World Maker.bat".
3. CHOOSE IMAGE.
4. Select zoom range if the defaults are not suitable.
5. Select MBTiles, TPKX, or Both.
6. Choose output name/folder.
7. BUILD RASTER PYRAMID.
8. Leave the Factory running until COMPLETE.

AUTOMATIC BEHAVIOR
- Real CRS/geotransform present: preserves real georeferencing.
- Ordinary flat image: creates synthetic projected display placement automatically.
- Flat images are parked near 30N, 80W in the Atlantic east of Florida.
- Since v0.2.0 flat pictures use photo mode (Pillow, no QGIS). On the QGIS route, giant flat images are decoded once into a temporary tiled working GeoTIFF with overviews before QGIS rendering.
- Original source raster is never modified.

LONG JOBS
v0.1.3 displays a changing heartbeat, elapsed time, stage name, and the most recent meaningful worker message. QGIS percentages are shown only when QGIS actually provides them.

FROZEN RENDERING BASELINE
QGIS 3.44.9
PNG
96 DPI
Antialiasing ON
Metatile 4

TPKX
The included MBTiles_to_TPKX_v0_3_0.py (v0.1.5) writes the same TPKX structure as mb2tpkx 1.1, which is proven in ArcGIS Earth and ArcGIS Pro. Its fingerprint is checked by the self-test. Do not casually rewrite it.

THIS IS A TEST BUILD
v0.1.3 is LIVE-PROVEN. v0.1.5 made the TPKX step write the same structure as mb2tpkx 1.1 (ArcGIS Earth / Pro proven). v0.1.6 fixes: the Cancelled message, Cancel stopping QGIS at once, closing the window mid-build (now stops QGIS and cleans up first), TPKX max zoom 23 checked before building, and a typed-in image path being inspected. Still open for live proof: real-georaster AUTO mode and broader giant-raster coverage.

PHOTO MODE (v0.2.0)
Photos and other flat pictures are now tiled directly - no QGIS needed, much faster, and TPKX files about a quarter of the size (JPEG tiles). QGIS is only needed for real map rasters (GeoTIFFs with coordinates). The first start installs the Pillow helper automatically. Settings: [PHOTO] in System Files\Picture_World_Maker_Config.ini.

ZOOM LIMIT FOR TPKX
TPKX (Esri tile packages) go up to zoom 23. For MBTiles only, up to 25 is allowed.
