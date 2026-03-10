"""
-= Definitions / Concepts
"""

from pathlib import Path # Import Path
from io import open # Import open

# Refer to path with raw string (Ignore backlash for escape characters)
path = Path("chapter_8.py")  # Create path (Is only a refer, it can exists or not)
home_path = Path.home()  # Return home path
print(path.is_file())  # Check if path is file (Return boolean)
print(path.is_dir())  # Check if path is directory (Return boolean)
print(path.exists())  # Check if path exists (Return boolean)
print(
    path.name,  # Return filename +  extension
    path.stem,  # Return filename
    path.suffix,  # Return extension
    path.parent,  # Return parent directory
    path.absolute(),  # Return absolute path
)
print(path.with_name("new_chapter_8.py"))  # Change filename with extension
print(path.with_suffix(".js"))  # Change extension
print(path.with_stem("new_chapter"))  # Change filename
file = open("chapter_8.py", "w") # Open file in write mode (If file doesn't not exist, python will create)
file.write("example") # Write file (We need to save it)
file.close() # Close and save the file with changes
file_2 = open("chapter_9.py", "r") # Open file in read mode (Default mode)
content = file_2.read() # Read file
content_list = file_2.readlines() # Read text and separate it in lines inside of list
with open("chapter_1.py") as file_3: # Use with statement (Will close the file if an error appear or we execute successfully our logic)
    print("File open")
