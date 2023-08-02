@ECHO OFF
REM start spoofer
TITLE Spoofer starter
COLOR 0A
MODE CON COLS=80 LINES=20
ECHO.
ECHO Starting...
ECHO Install requipts...
ECHO ----------------------------------------------------------------
pip install wget
ECHO ----------------------------------------------------------------
ECHO Starting...
python spset.py
ECHO Starting spoofer...
ECHO ----------------------------------------------------------------
