"""
-= Definitons / Concepts =-

- Exception: It is a error that interrupts the normal flow of the code.

"""

# Use try/except, this will try to execute the code inside 
# of the statement "try" and if this gets a error will execute de
# "except" statement
try: 
    n1 = int(input("Enter a number:"))
except:
    print("Error, the input was not a number")