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

- cls: Work in the same way as "self" but in this time the reference is for the class.

- Factory Method: Is a class method that help us to create multiple instance from class
with default values that we defined inside of the factory method, so we dont have to give
everytime the instance properties for the constructor.

- Private Properties: This properties can only be accessed within class or
method, not from outside.

- @property: Is a decorator that transform method to a class propertie, this is
useful to implement logic inside and validate some rules to set a specific propertie.
Python creates a property with the same name of the method, this property now has "fget" (Getter),
"fset" (Setter) and "fdel" (Deleter), so inside of the class create a "property object" that has all this
stuff where we can set all this methods mentioned before.
"""

# Create class
class Car:
    country = "USA" # Declare class propertie

    def __init__(self, brand, color ,n_wheels): # Create constructor
        self.brand = (brand) # Declare instance propertie
        self.color = color # Declare instance propertie
        self.__n_wheels = n_wheels # Declare private propertie (Only accessible inside of the class or method)

    @property # Set property (Getter)
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        if brand.strip():
            self.__brand = brand

    @classmethod
    def factory(cls): # Declare factory method
        return cls("Chevrolet", "Red", 4)
    
    @classmethod
    def turn_on(cls): # Declare class method
        print("Car turned on")
    
    def open_door(self): # Declare instance method
        print("Door opened")
    
    def __example_private(self): # Declare private method
        print(f"Private: {self.__n_wheels}") # Access to private propertie

my_car = Car("Toyota", "Red", 4) # Create object/instance class
my_car.open_door() # Call instance method
print(isinstance(my_car, Car)) # Check if object is a instance of the class (Return boolean)
print(my_car.brand) # Get instance propertie value
print(Car.country, my_car.country) # Get class propertie value (From class and from instance)
Car.turn_on() # Call class method
factory_car = Car.factory() # Create a instance with factory method
print(my_car.__dict__) # Get all properties from instance