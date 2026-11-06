@echo off
setlocal
cd /d "%~dp0"
set PYTHONDONTWRITEBYTECODE=1

rem --- v0.2.0: photo mode needs Pillow - install it once if it is missing ---
where py >nul 2>nul
if %errorlevel%==0 (
  py -3.14 -c "import PIL" >nul 2>nul
  if errorlevel 1 (
    echo Pillow is not installed yet. Installing it now - one time only...
    py -3.14 -m pip install Pillow
    py -3.14 -c "import PIL" >nul 2>nul
    if errorlevel 1 (
      echo.
      echo Pillow could not be installed automatically.
      echo Open Command Prompt and run:  py -3.14 -m pip install Pillow
      echo If your network blocks downloads, ask IT to install Pillow for Python 3.14.
      echo Rasta still works for real map rasters through QGIS.
      pause
    )
  )
)

where pyw >nul 2>nul
if %errorlevel%==0 (
  start "" pyw -3.14 "START RASTA PYRAMID FACTORY.pyw"
  exit /b 0
)

where pythonw >nul 2>nul
if %errorlevel%==0 (
  start "" pythonw "START RASTA PYRAMID FACTORY.pyw"
  exit /b 0
)

echo Python 3.14 GUI launcher was not found.
echo Install Python 3.14.5, then try again.
pause
endlocal
