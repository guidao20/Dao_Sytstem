xcopy /Y D:\python_program\pyqt5\Dao_system\*.py D:\python_program\pyqt5\Dao_system\exe\
TIMEOUT /T 2
::call activate pyqt5
::TIMEOUT /T 2
::D:
::cd D:\python_program\pyqt5\Dao_system\exe\dist
::del main_last.exe 
::TIMEOUT /T 2
::ren main.exe main_last.exe
::del /Q D:\python_program\pyqt5\Dao_system\exe\build\main\*
