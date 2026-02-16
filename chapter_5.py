"""
-= Definitions / Concepts =-

- List: Is a data structure where we can save any data type and modify them.

- Tuple: Is a data structure where we can't modify the saved values.

- Set: Is a data connection that cannot be repeated and is not oredered. Also
we cannot access to the elements inside but we can ask if the element is there.

- Dictionary: Is a data connection that is stored with key/value structure.

- When use lambda functions?: When the function or the proccess is needed
one time, if the action is needed more than one time is better to use a function.

- Row: Is a data structure that use FIFO statement (First in first out), that means that
we take first element and operate with it, after that the same with the second one and so
on up to N elements.

- Stack: Is a data structure that use LIFO statement (Last in first out), that means that we take
last element and operate with it, after that the same with de previous element and so on up to
N elements.
"""

from collections import deque

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

# -= Tuples =-
example_tuple = (1, 2, "example") # Declare tuple
joining_tuple = example_tuple + (3, 4) # Join tuples
example_tuple_two = tuple([1, 2]) # Create a tuple based on a iterable element

# -= Sets -=
example_set = {1, 2, 3}
print(example_set.add(4)) # Add a element
print(example_set.remove(1)) # Remove a element (Based on element, not index)
example_set_two = set(example_tuple) # Create a set based on a iterable element
print(example_set | example_set_two) # Join two sets (Union operator)
print(example_set & example_set_two) # Intersect two sets (Only keeps shared elements)
print(example_set - example_set_two) # Create a set with left set differences (Difference operator)
print(example_set ^ example_set_two) # Create a set with no shared elements (Symmetrical difference operator)

# -= Dictionaries =-
example_dict = { # Declare dict
    "a": 1,
    "b": 2
}
print(example_dict["a"]) # Access to a value by key (This can give us a error if the key does not exists)
print(example_dict.get("a")) # Access to a valye by key (If key does not exists return None)
example_dict["c"] = 3 # Add key/value
del(example_dict["c"]) # Delete element
print(example_dict.items()) # Get key/value pair in tuples

# -= Unpacking Operator =-
print(*example_list) # Use unpacking operator (Extract all elements from list/tuple)
print([*example_list, *example_list_two]) # Create new list with unpacking operator
print({**example_dict, **example_dict}) # Create new dict with unpacking operator

# -= Rows =-
row = deque([1, 2, 3]) # Create a row with deque
print(row.append(4)) # Add element to row
print(row.popleft()) # Remove respective element

# -= Stack (Is a list but with stack logic [LIFO])=-
stack = [1, 2, 3] # Declare stack/list
print(stack.pop()) # Remove respective element
print(stack.append(3)) # Add respective element
