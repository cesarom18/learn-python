"""
-= Definitions / Concepts =-

- Variable: When we create a variable python
(And other languages) asign a space in RAM, so
when python or our app need this variable it will
only make a reference to this space and recover the variable
value.

- Argument: Is the value that we pass to functions.

- Method: A function that is inside of object (Previously created by class).
"""

# -= How Declare Variable (Simple and multiple) =-
age = 18
name, surname = "example1", "example2"

# -= Basic Types (Primitives) =-
city = "Example" # String type
number = 1 # Integer type
score = 2.8 # Float type
imaginary = 1 + 3j # Complex type
is_true = False # Boolean type
is_void = None # None type

# -= Strings =-
multi_text = """This is a multi line text""" # Declare multi-line string
print(len(city)) # Get elements count (In this case 6 elements/characters)
print(multi_text[0]) # Get specific character (Start from index 0)
print(multi_text[0:4]) # Slice string (The first index is the start and de last one is where we need to end the slice)
format_string = f"{city} {number}" # Create format string (Inside of keys we can put any expresion)
print(city.upper()) # Method to transform all characters to uppercase
print(city.lower()) # Method to transform all characters to lowercase
