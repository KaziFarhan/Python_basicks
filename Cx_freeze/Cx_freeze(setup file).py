#you need to put it in same dir or use the path
from cx_Freeze import setup, Executable

setup(name='myexe',version='0.1',description='stuff',executables=[Executable('studier_no_gui.py')])         #could use path in Executable('path')

# should ron it with command "python setup.py(is thats the name of this setup) buil"
