@ECHO OFF

SET PYTHONPATH=%~dp0\..\webserver\properform\python

CALL python -B -m cProfile -o demo.prof src\demo.py
CALL python -B %~dp0\commit.py demo.prof
DEL /F /Q demo.prof

@PAUSE
