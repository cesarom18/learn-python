"""
-= Definitions / Concepts =-

- Class: Is the base from every object (Class instance), is there where
we declare constructor and methods.

- Object: Is a class instance, to initialize a object we need to assign class contructor
to a variable and this brings all methods/properties that we delcare inside the class.

- Method: Function inside of the class.

- Constructor: Is a function that is executed every time we create a instance from class

- self: Is a reserved word that refer to object himself, that means every instance have a
different "self" to make every object unique in terms of memory location and logic of course.
In simple words is the same "variable" that we bring the class at the beginning.
"""

# Create class
class Car:
    country = "USA" # Declare class propertie

    def __init__(self, brand): # Create constructor
        self.brand = brand # Declare instance propertie

    def turn_on(self): # Declare method
        print("Car turned on")

my_car = Car("Toyota") # Create object/instance class
print(isinstance(my_car, Car)) # Check if object is a instance of the class (Return boolean)
print(my_car.brand) # Get instance propertie value
print(Car.country, my_car.country) # Get class propertie value (From class and from instance)