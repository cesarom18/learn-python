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

class CustomException(Exception): # Extend from some exception type
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
    
    def __str__(self):
        return f"{self.msg} - CODE: {self.code}"

def division(n=0):
    if n == 0:
        raise ZeroDivisionError("You cannot divide by 0") # Invoke exception from function
    return 5 / n

try:
    division()
except ZeroDivisionError as ex: # Use the invoke exception in try/expect statement
    print(ex)