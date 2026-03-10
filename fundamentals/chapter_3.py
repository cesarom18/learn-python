"""
-= Definitions / Concepts =-

- Expresion: Is a instruction chain that evaluate only one thing

- Short Circuit Operations: When we have a comparison between two or more
different condition (With and, or) always python evalute this from left to
right, so if the first condition end the comparison the others conditions
will not be evaluated. This is useful when we have heavy operations or process
and we only need to execute this proccess if is needed.

- Iterable: Anything that can be iterated and where each element is known.
"""
# -= Logic Operators =-
print(1 < 2) # Less than
print(1 > 2) # Greater than
print(1 <= 2) # Less or equal than
print(1 >= 2) # Greater or equal than
print(1 == 1) # Equal than
print(1 != 1) # Not equal than

# -= If / Else / Elif =-
age = 18
if age >= 18:
    print("Legal age")
elif age < 18:
    print("Not legal age")
else:
    print("Whatever")

# -= Ternary Operator =-
ternary_result = "Legal age" if age > 18 else "Not legal"

# -= Logic Operators =-
aux_bool = True
if age > 1 and age < 20: # And operator (All conditions need to be true)
    pass
if age > 20  or age == 18: # Or operator (Only one condition need to be true)
    pass
if not aux_bool: # Not operator (Denies condition)
    pass

# -= Loops =-
for n in range(5): # For loop
    pass

while aux_bool: # While loop
    pass
