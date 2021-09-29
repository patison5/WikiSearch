@echo off
echo Starting..
:main
.\venv\Scripts\python.exe .\HabrParser.py
echo Restarting Bot..
goto main