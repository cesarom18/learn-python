"""
-= Definitions / Concepts =-

- Variable: When we create a variable python
(And other languages) asign a space in RAM, so
when python or our app need this variable it will
only make a reference to this space and recover the variable
value.

- Argument: Is the value that we pass to functions.

- Method: A function that is inside of object (Previously created by class).

-Truthy/Falsy: Concept that python give us to evaluate some
data type, when we compare two different values (Waiting a boolean result)
or when whe convert some data types with boolean built-in function
"""

import math

# -= How Declare Variable (Simple and multiple) =-
age = 18
name, surname = "example1", "example2"

# -= Basic Types (Primitives) =-
city = "Example"  # String type
number = 1  # Integer type
score = 2.8  # Float type
imaginary = 1 + 3j  # Complex type
is_true = False  # Boolean type
is_void = None  # None type

# -= Strings =-
multi_text = """This is a multi line text"""  # Declare multi-line string
print(len(city))  # Get elements count (In this case 6 elements/characters)
print(multi_text[0])  # Get specific character (Start from index 0)
print(
    multi_text[0:4]
)  # Slice string (The first index is the start and de last one is where we need to end the slice)
format_string = (
    f"{city} {number}"  # Create format string (Inside of keys we can put any expresion)
)
print(city.upper())  # Method to transform all characters to uppercase
print(city.lower())  # Method to transform all characters to lowercase
print(city.capitalize())  # Method to transform the first letter into uppercase
print(city.title())  # Method to transform all first character in each word to uppercase
print(
    city.strip()
)  # Method to remove left and right blank spaces in the string (We can use lstrip for left blank spaces and rstrip for right)
print(
    city.find("a")
)  # Method to find character group, if find it return index otherwise -1
print(
    city.replace("a", "b")
)  # Method to replace characters, first arg is what we want to replace and the second arg is the what it will be replaced with

# -= Numbers =-
# Operations
print(1 + 1)  # Addition
print(1 - 1)  # Susbtract
print(1 * 1)  # Multipy
print(1 / 1)  # Division (With decimals)
print(1 // 1)  # Division (Without decimals)
print(1 % 1)  # Give us rest of division
print(1**1)  # Raise to power
# Math module
print(round(1.3))  # Round number
print(abs(-1))  # Return absolute number (Distance from 0)
print(math.ceil(1.1))  # Return nearest higher number
print(math.floor(1.1))  # Return nearest lower number
print(math.isnan(1))  # Return boolean if arg is a number or not
print(math.pow(2, 3))  # Same as operator "**"
print(math.sqrt(2))  # Return the square of number

# -= Type Conversion =-
print(str(1)) # Convert arg to string data type
print(int("1")) # Convert arg to int data type
print(float(1)) # Convert arg to float data type
print(bool(0)) # Convert arg to boolean data type
