"""
-= Definitons / Concepts =-

- Exception: It is a error that interrupts the normal flow of the code.

"""

# Use try/except, this will try to execute the code inside 
# of the statement "try" and if this gets a error will execute de
# "except" statement
try: 
    n1 = int(input("Enter a number:"))
except ValueError as ex: # "ValueError" is a exception type from "Exception" class
    print(ex) # Error message
    print("Error, the input was not a number")
else: # "else" statement to execute always if there is no errors in main code flow
    print("Example")
finally: # "finally" statement to execute always, doesn't matter if throw error
    print("Example")