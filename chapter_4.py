"""
-= Definitions / Concepts =-

- Parameter: It is a variable within the function that
we can refer to

- Argument: It is the value that we pass to the function
parameter
"""

# -= Functions =-
def example_function(example_param, default_param = "example"): # Declar a function with parameters
    print(example_param)

example_function(example_param="example") # Pass named argument

def xarg(*numbers): # Xargs (Create a list with all given args)
    print(numbers) # List
    return numbers

def kwarg(**example_kwarg): # kwarg (Create a dictionary with all given args [This args must be named])
    print(example_kwarg) # Dict
    return example_kwarg