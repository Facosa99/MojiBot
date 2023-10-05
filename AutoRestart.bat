@echo off
echo Starting..
:main
.\MojiEnviroment\Scripts\activate
MojiBot.py
echo It seems MojiBot has crashed
echo Restarting...
goto main