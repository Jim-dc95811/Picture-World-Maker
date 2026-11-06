# Operator Workflow

## Normal workflow

1. Install the frozen supported QGIS and Python versions.
2. Extract the entire Picture World Maker package.
3. Launch `Start Picture World Maker.bat`.
4. Click **CHOOSE IMAGE** and select the source raster.
5. Review the automatically detected raster dimensions and the proposed zoom range.
6. Choose the finished product: **MBTiles**, **TPKX**, or **Both**.
7. Choose the output folder/name.
8. Click **BUILD RASTER PYRAMID**.
9. Leave the Factory running until it reports **COMPLETE**.

## Signs of life

v0.1.3 adds a continuously changing working line during long operations. It reports:

- elapsed time;
- current manufacturing stage;
- a changing heartbeat symbol;
- QGIS progress when QGIS exposes trustworthy numeric progress.

A long raster operation must never look dead merely because the underlying engine is between measurable progress callbacks.

## Long-build rule

Do not start a second Picture World Maker instance or edit/delete the source/output while a build is active. Use **CANCEL** if the job must be stopped; Picture World Maker terminates the active subprocess tree and cleans temporary manufacturing state.

## Flat image versus real georaster

There is no normal-user choice. Picture World Maker inspects the input automatically:

- valid CRS + valid geotransform → preserve real georeferencing;
- otherwise → use Picture World Maker's synthetic display placement.

The original source file is not modified in either case.
