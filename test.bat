@ECHO OFF

SET PYTHONPATH=%~dp0\..\webserver\properform\python

CALL python -B src\demo.py
CALL python -B %~dp0\commit.py localhost/app/properform/profile 0b37c65b380753a0bad936678ba9e682 demo.profile, demo.memleak
DEL /F /Q demo.profile
DEL /F /Q demo.memleak

@PAUSE
