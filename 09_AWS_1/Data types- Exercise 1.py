# Exercise 4

# Assign values to variables a, b, c, and d.
a = 'int'
b = 7
c = False
d = "18.5"

# Determine the data types of all four variables using the built-in type() function.
type_a = type(a)
type_b = type(b)
type_c = type(c)
type_d = type(d)

# Print the data types of variables a, b, c, and d.
print("Data type of a:", type_a)
print("Data type of b:", type_b)
print("Data type of c:", type_c)
print("Data type of d:", type_d)

# Make a new variable x and give it the value b + d.
# This will initially raise an error due to trying to add an int and a string.

# Fix the error by converting the string d to a float before performing the addition.
x = b + float(d)

# Print the value of x.
print("Value of x:", x)

