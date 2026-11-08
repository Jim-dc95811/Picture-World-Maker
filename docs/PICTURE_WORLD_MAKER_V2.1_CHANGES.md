# Picture World Maker 2.1 - what changed

**Released 2026-11-08** after Jim's live test in ArcGIS Earth (re-hardening pass). Download: [`Picture_World_Maker_v2.1.zip`](../releases/Picture_World_Maker_v2.1.zip) SHA-256 `6dc5542d8bbbb7f0efda167dc563b99fd659c78baf6509e71433a5c14d5194c1`. The 2.0 zip is in [`archive/`](../archive/).

Ordinary pictures (8-bit JPEG / PNG / TIFF without see-through parts or a turn mark) make **byte-identical tiles** to 2.0, so nothing you already built changes.

| # | Before (2.0) | Now (2.1) |
|---|---|---|
| 1 | A phone photo taken upright was built **lying on its side** (phones save the pixels sideways plus a turn mark that 2.0 ignored). | The turn mark (EXIF Orientation) is followed: the picture is built upright and the window shows its upright size. |
| 2 | 16-bit pictures (scans, HiRISE and other science pictures) came out **almost all white**. | They are stretched to normal brightness (darkest 0.1 % -> black, brightest 0.1 % -> white). |
| 3 | See-through parts of a PNG came out **black**. | They come out **white**. |
| 4 | A file with the same name stopped the build with only a file path. | The window asks **"... already exists. Replace it?"** - Yes builds over it, No keeps it. |
| 5 | No disk-space check: a full drive failed at the end of a long build. | Space is checked **before** any work (about 20 KB per tile + 200 MB), with a plain message. |
| 6 | The default folder was `C:\Users\<you>\Desktop`, which is not your Desktop when OneDrive moved it. | The default folder is your **real Desktop**, asked from Windows. |

## Live test (Jim, 2026-11-08)

Test kit `Picture_World_Maker_v2.1_TEST.zip` with three pictures: TEST_1 sideways phone photo ("THIS WAY UP" read the right way in ArcGIS Earth), TEST_2 16-bit grey (grey wave pattern, not white), TEST_3 see-through PNG (blue card on white), plus the Replace question. The disk-space check needs a nearly full drive, so it was proven by the test rig only.

## Proof here

- Rig [`tools/test-rigs/picture_world_maker_test_v21.py`](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/blob/main/tools/test-rigs/picture_world_maker_test_v21.py) (ArcGIS Earth Unlocked): 2.0 vs 2.1, ALL PASS - 8-bit JPEG and PNG tiles byte-identical; phone photo upright; 16-bit mean brightness 127 of 255; see-through corner white with the art unchanged; Replace path; disk check stops before building.
- `PWM_SELF_TEST.py`: PASS, with new checks for all of the above.

## Code

- `PWM_PHOTO_TILER.py`: `orientation`, `upright_size`, `_stretch_high_bit`, `prepare_picture` (used by `build_photo_mbtiles` in place of `convert("RGB")`).
- `PWM_PIPELINE.py`: `inspect_raster_pillow` uses the upright size; `space_needed`, `check_disk_space`; `build(..., replace_existing=False)` with a plain "already exists" message.
- `PICTURE_WORLD_MAKER.py`: `VERSION = "2.1"`, `desktop_dir()`, Replace question in `start_build`.

## Known, not changed

The Name box fills in only when it is empty, so a second picture chosen in the same session keeps the first picture's name - type the new name yourself (noted in the manual).
