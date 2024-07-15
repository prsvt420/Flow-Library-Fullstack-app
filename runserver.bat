@ECHO OFF

CD flow_library_server && start cmd.exe /K django-run.bat
CD ..\flow_library_client && start cmd.exe /K vue-run.bat

EXIT