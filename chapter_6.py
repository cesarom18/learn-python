"""
-= Definitions / Concepts =-

- Class: Is the base from every object (Class instance), is there where
we declare constructor and methods.

- Object: Is a class instance, to initialize a object we need to assign class contructor
to a variable and this brings all methods/properties that we delcare inside the class.

- Method: Function inside of the class.
"""

# Create class
class Car:
    def turn_on(self): # Declare method
        print("Car turned on")

my_car = Car() # Create object/instance class
print(isinstance(my_car, Car)) # Check if object is a instance of the class (Return boolean)