@echo off
cd /d "%~dp0"

if not exist ".venv" (
    echo Setting up (first run only)
    python -m venv .venv
    .venv\Scripts\pip install -q -r requirements.txt
)

rem --- Make sure a C++ compiler is available. If g++ is already on PATH,
rem     or we've previously auto-installed one, skip straight to launching.
where g++ >nul 2>nul
if %errorlevel%==0 goto :havegpp
if exist "tools\gpp_path.txt" goto :havegpp

echo.
echo No C++ compiler found on your system.
echo Downloading a portable one (about 150MB, one-time only, needs internet)...
echo.

if not exist "tools" mkdir "tools"

powershell -NoProfile -Command ^
    "try { Invoke-WebRequest -Uri 'https://github.com/brechtsanders/winlibs_mingw/releases/download/16.1.0posix-14.0.0-ucrt-r3/winlibs-x86_64-posix-seh-gcc-16.1.0-mingw-w64ucrt-14.0.0-r3.zip' -OutFile 'tools\mingw_download.zip' -UseBasicParsing } catch { exit 1 }"

if not exist "tools\mingw_download.zip" (
    echo.
    echo Download failed -- check your internet connection and try again later.
    echo You can still use the Python track in the meantime.
    echo.
    goto :havegpp
)

echo Extracting...
powershell -NoProfile -Command "Expand-Archive -Path 'tools\mingw_download.zip' -DestinationPath 'tools' -Force"
del "tools\mingw_download.zip"

set "GPPPATH="
for /f "delims=" %%i in ('dir /s /b "tools\g++.exe" 2^>nul') do set "GPPPATH=%%i"

if defined GPPPATH (
    > "tools\gpp_path.txt" echo %GPPPATH%
    echo.
    echo C++ compiler installed successfully.
    echo.
) else (
    echo.
    echo Something went wrong -- couldn't find g++.exe after extracting.
    echo You can still use the Python track. Delete the tools\ folder and
    echo re-run this script to retry the download.
    echo.
)

:havegpp
.venv\Scripts\python app.py
