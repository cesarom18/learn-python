"""
-= Definitions / Concepts =-

- Modules: Related parts of code, functions or variables that can be exported
to other files in a application.

- Module cache (__pycache__): This folder contains all pre-compiled code of all python modules created to improve
the app performance, if the module change his modify date then python will replace the module cache again.

- Package: The main difference between module and package is that package is a do reference to a folder,
to transform a folder into a package we need to create a "__init__.py" file.

- "__main__": With this Python tell us which file is executing in the
"main" thread, so if we execute specifically one file this will contain
on his "__name__" the value of "__main__".
"""
import math

print(dir(math)) # Use function dir (This give us some magic functions and related packages)
