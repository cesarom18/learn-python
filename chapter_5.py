"""
-= Definitions / Concepts =-

- List: Is a data structure where we can save any data type.

- Tuple: Is a data structure where we can save only one data type.
"""

# -= List =-
example_list = [1 ,2] # Declare list
example_list_two = [0] * 10 # Multiply the content inside of the list X times
join_list = example_list + example_list_two # Join lists
numbered_list = list(range(5)) # Create numbered list with list constructor
char_list = list("example") # Create char list based by string
print(example_list[0]) # Get list element
example_list[0] = 3 # Change element list   
print(example_list[0:1]) # Slice list (start, end, step)
first_element, *others = example_list_two # Unpack elements from list
print(enumerate(example_list)) # Create a list with tuples, each tuple has index and respective value
print(example_list.index(1)) # Find a element and return his index (First ocurrency), otherwise return error
print(example_list.count(1)) # Count how many time a element is in the list
