"""
-= Definitions / Concepts
"""

from pathlib import Path

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
