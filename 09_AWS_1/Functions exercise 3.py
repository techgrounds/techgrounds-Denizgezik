# Exercise 3

# Define the avg() function to calculate the average of two numbers.
def avg(a, b):
    return (a + b) / 2

# I am not allowed to edit any code below here.

# Given values
x = 128
y = 255

# Calculate the average using the avg() function.
z = avg(x, y)

# Print the result.
print("The average of", x, "and", y, "is", z)


def avg(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Given values
numbers = [128, 255]

# Calculate the average using the avg() function.
z = avg(numbers)

# Print the result.
print("The average of", numbers, "is", z)
