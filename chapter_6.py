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

- "Magic Method"?: Is a method that will be executed indirectly.

- Class Container: The meaning of this concept is when class contains multiple instance from other class
(Normally in a list), like a massive storage.

- Inheritance: When we use inheritance all properties and methods will be available for the children class, and when
we declare a multiple inheritance and we have the same named method or propertie the children class will take the last
one declared from the fathers class (From right to left)

- Overweight: This happens when we have the same method in two class (When we use inheritance of course)
and the sub-class keeps with his own method implementation overwritting the father method class.
"""

class Concessionaire:
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars
    
    def add_car(self, car):
        self.cars.append(car)
    
    def show_cars(self):
        for car in self.cars:
            print(car)

# Create class
class Car:
    country = "USA" # Declare class propertie

    def __init__(self, brand, color ,n_wheels): # Create constructor (Magic method)
        self.brand = brand # Declare instance propertie
        self.color = color # Declare instance propertie
        self.__n_wheels = n_wheels # Declare private propertie (Only accessible inside of the class or method)

    def __del__(self): # Call destructor (When instance get eliminated)
        print("Auto eliminado")
    
    def __str__(self): # Magic method to change how is printed a instance
        return f"Brand: {self.brand} | Color : {self.color}"
    
    def __eq__(self, to_compare): # Magic method to known if two instances are the same in properties values
        return self.brand == to_compare.brand and self.color == to_compare.color
    # When we define "__eq__" automatically python infers the opposite magic method (__ne__)
    def __ne__(self, to_compare): # Magic method to known if two instances are not the same in properties values
        return self.brand != to_compare.brand and self.color != to_compare.color
    # When we define "__lt__" automatically python infers the opposite magic method (__gt__)
    def __lt__(self, to_compare): # Magic method to known if two instances are lower than in some propertie value
        return self.__n_wheels < to_compare.__n_wheels
    # When we define "__le__" automatically python infers the opposite magic method (__ge__)
    def __le__(self, to_compare): # Magic method to known if two instances are lower or equal than in some propertie value
        return self.__n_wheels <= to_compare.__n_wheels

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
# del my_car # Delete instance
concessionaire = Concessionaire("Example", [my_car])
concessionaire.show_cars()

class Animal:
    def __init__(self):
        self.name = "Example"

    def walk():
        print("Animal walking")
    
    def jump():
        print("Animal jumping")

class Dog(Animal):
    def __init__(self):
        super().__init__() # Call father class constructor
        self.something = True

    def walk(): # Annulment method (Overweight)
        super().walk() # Call father class method
        print("Dog walking")