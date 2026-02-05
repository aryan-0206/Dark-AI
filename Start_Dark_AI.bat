@echo off
setlocal enabledelayedexpansion

:: Change to the directory where the script is located to ensure paths work
cd /d "%~dp0"

title Dark AI - Voice Assistant [Starting...]

echo =======================================================
echo          DARK AI - PREMIUM VOICE ASSISTANT
echo =======================================================
echo.

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not detected! 
    echo Please install Python and ensure 'Add to PATH' is checked.
    pause
    exit /b 1
)

:: Check for .env file
if not exist ".env" (
    echo [WARNING] .env file not found! 
    echo Creating .env from template...
    if exist ".env.template" (
        copy ".env.template" ".env"
        echo [INFO] Created .env. Please add your API keys to it for full functionality.
    ) else (
        echo [ERROR] .env.template also missing. AI features may not work.
    )
    echo.
)

:: Clean up any hanging python processes for a smooth start
echo [1/3] Preparing environment...
taskkill /f /im python.exe /fi "WINDOWTITLE ne Dark AI*" >nul 2>&1

:: Install/Update dependencies
echo [2/3] Checking requirements...
pip install -r requirements.txt --quiet --no-warn-script-location

echo.
echo [3/3] Launching Dark AI Server...
echo -------------------------------------------------------
echo  - Web Interface: http://127.0.0.1:5000
echo  - Status: Everything is running smooth!
echo  - Tip: Keep this window open while using Dark AI.
echo -------------------------------------------------------
echo.

:: Run the flask app
:: The browser will open automatically via python script
python flask_app.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] The application crashed or was stopped.
    echo Check the messages above for details.
    pause
)
