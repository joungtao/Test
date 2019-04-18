@ECHO OFF

SET PYTHONPATH=%~dp0\..\webserver\properform\python

CALL python -B -m cProfile -o demo.prof src\demo.py
CALL python -B %~dp0\commit.py localhost 0b37c65b380753a0bad936678ba9e682 demo.prof
DEL /F /Q demo.prof

@PAUSE
