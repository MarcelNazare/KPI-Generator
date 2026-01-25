@echo off
REM kpi_gen.bat - wrapper to call main.py with a file location and optional file name
REM Usage: kpi_gen.bat "C:\path\to\directory_or_file" "optional_filename.csv"
REM Activate the virtual environment
call C:/Users/marcel/Desktop/KPI Generator/.venv/Scripts/activate.bat
REM Change working directory to the script location (project root)
pushd "%~dp0" || (
  echo Failed to change directory to script folder "%~dp0"
  exit /b 1
)

REM Ensure at least one argument (file location) is provided
if "%~1"=="" (
  echo Usage: %~n0 "file_location" [file_name]
  echo Example: %~n0 "C:\Users\marcel\Desktop\KPI Generator\sample data" "dim_geography.csv"
  popd
  exit /b 1
)

REM Capture args (expanded without surrounding quotes)
set "FILE_LOCATION=%~1"
set "FILE_NAME=%~2"

REM Defensive cleaning: remove any stray '>' characters (users sometimes paste prompts)
set "FILE_LOCATION=%FILE_LOCATION:>=%"

echo Calling Python script with:
echo   file location: "%FILE_LOCATION%"
if not "%FILE_NAME%"=="" (
  echo   file name:     "%FILE_NAME%"
)

REM If FILE_NAME supplied, pass both flags; otherwise pass only file_path
if "%FILE_NAME%"=="" (
  uv run main.py --file_path "%FILE_LOCATION%"
) else (
  uv run main.py --file_path "%FILE_LOCATION%" --file-name "%FILE_NAME%"
)

set "EXITCODE=%ERRORLEVEL%"
popd
exit /b %EXITCODE%
