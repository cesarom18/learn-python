"""
-= Definitions / Concepts =-

- List: Is a data structure where we can save any data type.

- Tuple: Is a data structure where we can save only one data type.

- When use lambda functions?: When the function or the proccess is needed
one time, if the action is needed more than one time is better to use a function.
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
print(example_list.insert(1, 1)) # Insert a element into list in the specified index (Move all elements one index up)
print(example_list.append(2)) # Add a element at the end of list
print(example_list.remove(1)) # Delete first ocurrency element of the list
print(example_list.pop()) # Delete the last element of the list if we dont give a specific index
del example_list[0] # Delete a specific element by index
print(example_list.clear()) # Clear all list
print(example_list.sort()) # Sort all elements
print(sorted(example_list)) # Return sorted list

# -= Lambda Expresions =-
print(example_list.sort(key=lambda el:el[0])) # Declare and use lambda (Params:Return)

# -= Compression List =-
example_compression = [element * 2 for element in example_list] # Element Return/Element/Iterable
example_compression_two = [element for element in example_list if element > 0] # Comression list with condition

# -= Map / Filter =-
example_map = list(map(lambda element: element *2, example_list)) # Use map(function, iterable)
example_filter = list(filter(lambda element: element > 0, example_list)) # Use filter(function, iterable)
