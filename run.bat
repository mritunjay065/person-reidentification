@echo off
title Computer Vision Project Launcher
cd /d "%~dp0"
echo Starting Project Launcher...
echo.

REM Use the virtual environment Python
set VENV_PYTHON=c:\Users\mritu\OneDrive\Desktop\testing\.venv312\Scripts\python.exe

if exist "%VENV_PYTHON%" (
    "%VENV_PYTHON%" launcher.py
) else (
    echo Virtual environment not found at: %VENV_PYTHON%
    echo Trying system Python...
    python launcher.py
)

pause
