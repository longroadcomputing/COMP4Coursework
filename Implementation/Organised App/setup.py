# This is the Demo voersion of the Application to be built for media department of Cambridge Community Church.
# This Software is not complete and as a result there are areas that are not yet fully functional.

# Use of this software is restircted for DEMONSTRATION USESS ONLY!

# Copyright Joel Butcher 2015 ©

application_title = "Database Management System" #what you want to application to be called
main_python_file = "Main.py" #the name of the python file you use to run the program
application_version = "0.1"
application_description = "SQLite Inspector alls you to view data, execute queries and see entity descriptions"
windows_icon = "Database.ico"
mac_icon = "Database.icns"

import sys
import os

from cx_Freeze import setup, Executable

base = None

includes = ["atexit","re"]

if sys.platform == "win32":
    base = "Win32GUI"
    include_files = [("C:\Python32\Lib\site-packages\PyQt4\plugins\sqldrivers","sqldrivers")]
    build_options = {"path": sys.path,
                 "includes": includes,
                 "include_files":include_files,
                 "icon":windows_icon
                }
else:
    include_files = [("/opt/local/share/qt4/plugins/sqldrivers","sqldrivers")]
    build_options = {"path": sys.path,
                 "includes": includes,
                 "include_files":include_files
                }

if sys.platform == "win32":
    setup(
            name = application_title,
            version = application_version,
            description = application_description,
            options = {"build_exe" : build_options},
            executables = [Executable(main_python_file, base = base)])
else:
    setup(
            name = application_title,
            version = application_version,
            description = application_description,
            options = {"build_exe" : build_options},
            executables = [Executable(main_python_file, base = base, targetName= application_title)])