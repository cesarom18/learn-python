"""
-= Definitions / Concepts
"""
from pathlib import Path

file = Path("chapter_9.py") # Get file
print(file.exists()) # Check if file exists
print(file.rename("new_chapter_9.py")) # Rename file
print(file.unlink()) # Remove file
print(file.stat()) # Get file metadata (Size, access date, modify date)
print(file.read_text("utf-8")) # Read text from file
file.write_text("example", "utf-8") # Write file (Text, encoding)
