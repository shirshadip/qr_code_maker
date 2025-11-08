@echo off
echo -----------------------------------------
echo Installing Python qrcode module...
echo -----------------------------------------

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not added to PATH.
    echo Please install Python from https://www.python.org/downloads/ and try again.
    pause
    exit /b
)

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install qrcode and pillow
echo Installing required packages...
pip install qrcode[pil]

echo -----------------------------------------
echo Installation complete!
echo You can now use the qrcode module in Python.
echo -----------------------------------------
pause
