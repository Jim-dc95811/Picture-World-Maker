# Picture World Maker

> 🤖 **Using AI assistance?** Have the agent read the [CLAUDE.md](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/blob/main/CLAUDE.md) file first.

**Turn giant pictures into maps you can fly into.** Slice. Dice. Present.

## Get everything you need

**1. ⬇️ [ArcGIS Earth](https://www.esri.com/en-us/arcgis/products/arcgis-earth/downloads)** - free 3D globe from Esri (Windows desktop version), to look at and fly over the result.

**2. ⬇️ [Python 3.14](https://www.python.org/downloads/windows/)** - free; install with the default options.

> **First time? Three quick tips**
> 1. **Extract the zip first:** right-click the downloaded zip > **Extract All**, then open the new folder. Double-clicking files while they are still inside the zip does not work.
> 2. **Windows security warning:** Windows may warn about any program downloaded from the internet. Click **More info > Run anyway** (blue "Windows protected your PC" screen) or **Run**. To avoid the warning, right-click the zip > **Properties** > tick **Unblock** > **OK** before extracting.
> 3. **Installing Python:** if the installer shows **"Add python.exe to PATH"**, tick it.

### **⬇️ [3. DOWNLOAD PICTURE WORLD MAKER v2.1](releases/Picture_World_Maker_v2.1.zip)**
**📖 [User manual](docs/USER_MANUAL.md)**
**🗂️ [What's in the zip - every file explained](docs/images/picture_world_maker_whats_in_the_zip_full.png)**
**📦 [Download the Whole ArcGIS Earth Unlocked Series of Tools - all 10 in one zip](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/raw/main/downloads/ArcGIS_Earth_Unlocked_All_Tools.zip)**

Choose a giant picture - a city panorama, a scanned map, a schematic, artwork - press BUILD, and get a zoomable map (TPKX or MBTiles) you can open in ArcGIS Earth: see the whole scene like a hawk, then dive into any detail that catches your eye. **New in 2.1:** phone photos come out the right way up, 16-bit pictures no longer wash out to white, see-through parts turn white instead of black, it asks before replacing a file, checks the disk has room before it starts, and saves to your real Desktop (also the OneDrive one). [What changed in 2.1](docs/PICTURE_WORLD_MAKER_V2.1_CHANGES.md)

![Flying over a London panorama photo made with Picture World Maker in ArcGIS Earth: the photo lies flat on the Atlantic at 29.99 N, 80.05 W, elevation 0 ft, seen from 3,092 ft](docs/images/picture_world_kings_reach_arcgis_earth.jpg)

*A London panorama photo (50,000 x 12,006 pixels, 35,216 tiles) flown in ArcGIS Earth with EarthStick. A photo has no real location, so Picture World Maker parks it on the ocean off Jacksonville and gives it ocean coordinates - the status bar reads 29.99 N, 80.05 W, elevation 0 ft. That simulated georeferencing gives every spot in the picture its own latitude and longitude, so it behaves like a real map: zoom to full detail, put gates, beacons and objects on it, fly through it.*

![Sea, street, stone: the same London photo seen from 61,246 ft as a strip on the ocean, from 4,203 ft at street level with taxis and road markings, and from 786 ft beside the bell tower of St Paul's with people on its gallery](docs/images/picture_world_sea_street_stone.jpg)

*Sea, street, stone - one photograph, three heights. From 61,246 ft the whole panorama floats on the ocean like a postcard; at 4,203 ft you read the road markings and the ad on a taxi; at 786 ft you hover beside the bell tower of St Paul's and count the people on its gallery.*

**Fly into your pictures:** with [EarthStick](https://github.com/Jim-dc95811/EarthStick) you fly over the picture like a city; with [World Gate Maker](https://github.com/Jim-dc95811/EarthStick#make-your-own-gates) (ground elev 0) you can put gates that drop you onto any landmark in it. Or fly to the spot and pull the trigger with [EarthStick 1.3.6](https://github.com/Jim-dc95811/EarthStick#drop-gates-as-you-fly-new-in-136) - the Gate Dropper puts the gate right there.

![Photo mode, live-proven: the London panorama built in 55 seconds with no QGIS, then flown at street level in ArcGIS Earth](docs/images/picture_world_photo_mode_street.jpg)

*Photo mode (v0.2.0, live-proven 2026-11-06): the same 50,000 x 12,006 photo built in **55 seconds** with no QGIS (35,216 tiles; the QGIS route took 8:46) and a TPKX a quarter of the size (442 MB instead of 1.77 GB) - still sharp enough to read the street.*

`Picture_World_Maker_v0.2.4.zip` SHA-256: `b5b5ad4ac856ba992e413367039ab741d6e7b64e8c2b852ac1589f0358b7a3c6` - [what changed in v0.2.4](releases/v0.2.4_RELEASE_NOTES.md)

> **New in v0.2.4: 20 World spots - a gallery on the ocean.** Choose a **World spot** (1-20) in the window and each picture gets its own one-degree box of open Atlantic east of Florida, so many picture worlds can sit side by side. Spot 1 is where every picture landed before, so older files stay put. The file name says where it lives (`Tower_of_Babel_spot02.tpkx`), and the [spot list](docs/USER_MANUAL.md#world-spots-a-gallery-on-the-ocean) gives each spot's coordinates for World Gate Maker - one gate per painting makes an art tour.

![Two picture worlds on the ocean in ArcGIS Earth, seen from 339,729 ft: Bruegel's Tower of Babel on World spot 1 and the London panorama on World spot 2, one degree east](docs/images/picture_world_two_worlds_spot1_spot2.jpg)

*Live-proven 2026-11-06: Bruegel's* Tower of Babel *(public domain, 30,000 x 21,952 px) on World spot 1 and the London panorama on World spot 2 (built in 53 s, 35,205 tiles), side by side on the Atlantic. Jim: "Of all the crazy things to find floating in the Atlantic Ocean!!!"*

[![Babel to the Shard: Bruegel's treadwheel crane in the Tower of Babel (1563) beside the red tower cranes at the Shard in the London panorama - play the Short](docs/images/babel_to_shard_short_thumb.jpg)](https://www.youtube.com/shorts/lxvZLMLe-IY)

*Claude flies from Babel (World spot 1) to London (World spot 2): from Bruegel's wooden treadwheel crane, 1563, to the red tower cranes beside the Shard - 460 years of cranes. ▶️ [Watch the Short: ArcGIS Earth Babel to the Shard](https://www.youtube.com/shorts/lxvZLMLe-IY) (YouTube).*

> **No QGIS needed (v0.2.3).** Picture World Maker now does one thing: pictures. Real map files with coordinates (GeoTIFFs) open directly in ArcGIS Earth - drag them on.

> **New name (2026-11-06):** Picture World Maker was called **Rasta Pyramid Factory** up to v0.2.0. Same program, same files it makes; old download links in this repo's history still work.

> **ArcGIS Earth Unlocked:** Picture World Maker is the picture-to-map factory of the broader project family. See the [master system map](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked).

---

# Engineering record

*Picture World Maker was named Rasta Pyramid Factory up to v0.2.0; history below keeps the names used at the time where it matters.*

## Current version truth

### 2.1 — RE-HARDENING (2026-11-08) — current release

Live-tested by Jim 2026-11-08: a sideways phone photo built upright, a 16-bit picture built grey (not white), a see-through PNG built on white, the Replace question. Ordinary 8-bit pictures make byte-identical tiles to 2.0. See [what changed in 2.1](docs/PICTURE_WORLD_MAKER_V2.1_CHANGES.md).

### 2.0 — THE 2.0 REFERENCE (2026-11-08)

The whole ArcGIS Earth Unlocked family moved to 2.0 as one reference point ([2.0 Reference](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/blob/main/REFERENCE_2.0.md)). Picture World Maker 2.0 is the v0.2.4 program (World spots, below) with only its version text changed - the window says **PICTURE WORLD MAKER 2.0** and pictures come out exactly as before. The 2.0 zip and earlier zips are kept in [`archive/`](archive/).

### v0.2.4 — WORLD SPOTS (2026-11-06) — LIVE-PROVEN

Jim built the London panorama on spot 2 (53 s, 35,205 tiles, 25 bundles - the same counts as the test here) and flew it beside Bruegel's *Tower of Babel* on spot 1.

A **World spot** chooser (1-20): each picture can be parked in its own one-degree box of open ocean (30-31 N, 80-71 W), so a gallery of pictures can sit side by side. Spot 1 = the old parking spot; a spot-1 build is byte-identical to v0.2.3 (all 30 Kings Reach bundles). File names end in `_spotNN`. See [v0.2.4 release notes](releases/v0.2.4_RELEASE_NOTES.md).

### v0.2.3 — QGIS REMOVED (2026-11-06)

Photo mode is the only engine; the QGIS route, its worker and settings are gone (Jim: ArcGIS Earth opens GeoTIFFs directly). A GeoTIFF is built as a picture like any other. Photo builds are byte-identical to v0.2.2 (all 35,216 Kings Reach tiles). The QGIS-era sections below are history. See [v0.2.3 release notes](releases/v0.2.3_RELEASE_NOTES.md).

### v0.2.2 — ONE OBVIOUS FILE (2026-11-06)

After Extract All the folder holds just `Start Picture World Maker.bat` and `System Files`. The program is unchanged. See [v0.2.2 release notes](releases/v0.2.2_RELEASE_NOTES.md).

### v0.2.1 — NEW NAME (2026-11-06)

v0.2.0 photo mode with the new name; builds identical to v0.2.0 (0 structural differences). See [v0.2.1 release notes](releases/v0.2.1_RELEASE_NOTES.md).

### v0.2.0 — PHOTO MODE (2026-11-06) — LIVE-PROVEN

Jim's build 2026-11-06 00:47: Kings Reach panorama 1 in 55 s, 35,216 tiles, 30 bundles, flown in ArcGIS Earth. Flat pictures are tiled directly with Pillow - no QGIS. Kings Reach panorama 1: same 35,216 tiles and placement as v0.1.6, about 48 s instead of 8 min 46 s, TPKX 442 MB instead of 1.77 GB. Real map rasters keep the QGIS route. See [v0.2.0 release notes](releases/v0.2.0_TEST_RELEASE_NOTES.md).

### v0.1.6 — LIVE-PROVEN (2026-11-05)

Jim built `Kings_reach_panorama_1.jpg` (50,000 x 12,006 px, Z0-Z18, 35,216 tiles, 30 bundles, 8:46) and flew it in ArcGIS Earth: PASS. v0.1.5's TPKX fix (mb2tpkx 1.1 structure) plus five fixes from a full code review: the Cancelled message, Cancel stopping QGIS at once, closing the window mid-build (stops QGIS and cleans up first), TPKX max zoom 23 checked before building, typed-in image paths inspected. See [v0.1.6 release notes](releases/v0.1.6_TEST_RELEASE_NOTES.md).

### v0.1.5 TEST — BUILT / SELF-TESTED (2026-11-05)

The TPKX stage now writes the same structure as **mb2tpkx 1.1** (proven in ArcGIS Earth and ArcGIS Pro). Checked against Jim's flown London TPKX: 0 structural differences, all bundles byte-identical. Everything before the TPKX stage is the v0.1.3 LIVE-PROVEN baseline. Waiting for Jim's live test. See [v0.1.5 release notes](releases/v0.1.5_TEST_RELEASE_NOTES.md).

### v0.1.3 TEST — LIVE-PROVEN core

Picture World Maker v0.1.3 remains **LIVE-PROVEN** for:

- automatic flat-image / georaster inspection;
- tiled staging + overviews for giant flat images;
- headless QGIS 3.44.9 pyramid manufacturing;
- verified raster MBTiles;
- deterministic synthetic placement for ordinary flat images;
- long-build heartbeat;
- large/gigapixel workloads;
- TPKX output rendered successfully in **ArcGIS Earth**.

### TPKX converter — 2026-11-05

Since v0.1.6 Picture World Maker writes the same TPKX structure as mb2tpkx 1.1 (ArcGIS Earth and ArcGIS Pro proven).
---

## Current status

> Since v0.2.3 the QGIS rows below are history: the QGIS engine was removed and photo mode builds everything.

| Capability | Status |
| --- | --- |
| Automated giant-raster processing | ✅ **LIVE-PROVEN** |
| Headless QGIS 3.44.9 pyramid engine | ✅ **LIVE-PROVEN** |
| Raster -> verified MBTiles | ✅ **LIVE-PROVEN** |
| Historical MBTiles -> TPKX -> ArcGIS Earth | ✅ **LIVE-PROVEN** |
| v0.1.6 TPKX stage (mb2tpkx 1.1 structure) -> ArcGIS Earth | ✅ **LIVE-PROVEN 2026-11-05** |
| v0.2.0 photo mode (no QGIS) -> TPKX -> ArcGIS Earth | ✅ **LIVE-PROVEN 2026-11-06** (55 s) |
| Gigapixel-class deep navigation | ✅ **LIVE-PROVEN** |
| v0.1.3 synthetic placement + heartbeat | ✅ **LIVE-PROVEN** |
| v0.1.4 TPKX / MBTiles / REST selector | 🟡 **BUILT / SELF-TESTED HISTORICAL TEST BRANCH** |
| REST output | ⏸️ **PARKED** |

---

## Operator workflow

```text
1. Choose giant raster
2. Choose zoom range
3. Choose finished product(s)
4. BUILD RASTER PYRAMID
```

Picture World Maker distinguishes ordinary flat imagery from genuinely georeferenced raster input automatically. The normal operator does not need a CRS-mode selector or manual Georeferencer workflow.

The original source raster is not modified.

---

## Manufacturing architecture

> **v0.2.3:** the pipeline is now picture -> Pillow inspection -> photo-mode pyramid (MBTiles) -> TPKX converter -> verify -> publish. The QGIS steps shown below are the v0.1.x-v0.2.2 design, kept as history.

```text
giant source raster
-> QGIS/GDAL inspection
-> real georaster? -> preserve real georeferencing
       |
       no
       v
synthetic display placement
-> tiled working GeoTIFF + overviews
-> QGIS 3.44.9 headless pyramid engine
-> verified raster MBTiles
       |-- preserve MBTiles when selected
       `-- TPKX converter -> TPKX
```

### Current converter rule

For ArcGIS Earth, the v0.1.3 historical TPKX output remains proven evidence.

Since v0.1.6 Picture World Maker's TPKX stage writes the mb2tpkx 1.1 structure (proven in ArcGIS Earth and ArcGIS Pro; byte-identical bundles against Jim's flown London TPKX).

Do not rewrite the accepted v0.1.3 evidence package and pretend it was always the new converter.

---

## Major live proofs

### Montreal

- 29,684 x 7,620 pixels
- 13,381 raster tiles
- 52 bundles
- Z0-Z18
- 0:05:04
- ArcGIS Earth: PASS

### London — gigapixel-class

`Kings_reach_panorama_2.jpg`

- 63,000 x 18,589 pixels
- approximately 1.17 billion source pixels
- 67,619 final raster tiles
- Z0-Z18
- 30 bundles
- 0:23:07
- Windows File Explorer TPKX size: 1,949,149 KB
- ArcGIS Earth: PASS

Deep navigation resolved individual people inside London Eye observation pods.

### Barcelona

- 62,141 x 14,606 pixels
- approximately 908 million source pixels
- 52,482 final tiles
- Z0-Z18
- 30 bundles
- 0:20:40
- ArcGIS Earth: PASS

### Tower Bridge

- 15,287 x 7,643 pixels
- 6,976 tiles
- Z0-Z18
- 22 bundles
- 0:02:18
- Windows File Explorer TPKX size: 294,910 KB
- ArcGIS Earth: PASS

---

## Source-size lesson

A source file's compressed disk size is a poor predictor of pyramid size. Pixel dimensions, total pixel count, scene complexity, zoom range, and encoding matter more.

---

## Synthetic placement for ordinary images

A normal photograph has no honest geographic location. Picture World Maker labels its placement as **synthetic display space**.

Current reproducible rule:

```text
1 source pixel = 1 projected meter
working CRS = EPSG:3857
fixed synthetic Atlantic anchor near 30°N, 80°W
```

---

## Requirements

- Windows 10/11 64-bit
- Python 3.14.5 64-bit
- Pillow (installed by the launcher)

---

## Deployment boundary

Picture World Maker manufactures raster pyramids. It does not own field-delivery hardware.

Delivering maps to phones happens outside Picture World Maker.

---

## Project family

Picture World Maker is part of **[ArcGIS Earth Unlocked](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked)** - offline maps, joystick flight ([EarthStick](https://github.com/Jim-dc95811/EarthStick)), World Gates and objects for ArcGIS Earth. Picture World Maker is its picture-to-map factory.

---

## Documentation

- [User manual](docs/USER_MANUAL.md) ([PDF](docs/Picture_World_Maker_User_Manual.pdf))
- [Plain-language overview](docs/PLAIN_LANGUAGE_OVERVIEW.md)
- [Operator workflow](docs/OPERATOR_WORKFLOW.md)
- [Technical architecture](docs/TECHNICAL_ARCHITECTURE.md)
- [Live acceptance record](docs/ACCEPTANCE_RECORD.md)
- [Gigapixel + output-size guidance](docs/GIGAPIXEL_AND_OUTPUT_SIZE.md)
- [AI / maintainer restart note](docs/AI_CONTINUITY_RESTART_NOTE.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

---

## Human-AI engineering collaboration

Picture World Maker was conceived, directed and live-tested by **Jim Gaddy**, working with **OpenAI's ChatGPT** and **Anthropic's Claude** as AI coding and documentation partners. Jim supplied the idea of turning giant pictures into navigable pyramids, the QGIS recipe and every live Windows / ArcGIS Earth test. ChatGPT helped build Picture World Maker up to v0.1.4. Claude built v0.1.5-v0.1.6 (the mb2tpkx-structure TPKX stage, the code-review fixes, the structural self-test), the user manual and this page. See [CONTRIBUTORS.md](CONTRIBUTORS.md).

This acknowledgment is not a claim of OpenAI or Anthropic sponsorship or endorsement.

## Governing rule

> **Picture World Maker manufactures the pyramid. The real target decides compatibility. Do not let downstream deployment claims outrun evidence.**
