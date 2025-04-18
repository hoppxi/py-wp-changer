@echo off
:: Load environment variables from .env file
for /f "tokens=1,2 delims==" %%a in (.env) do (
    set %%a=%%b
)

:: Check if the WALLPAPER_PATH variable is set and then run the Python script
if defined WALLPAPER_PATH (
    pythonw "%WALLPAPER_PATH%\main.py"
) else (
    echo WALLPAPER_PATH not found in .env
)

pause
