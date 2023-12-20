# Exercise 2

# Write a custom function myfunction() that prints "Hello, world!" to the terminal.
def myfunction():
    print("Hello, world!")

# Call myfunction.
myfunction()

# Rewrite the function to take a string as an argument and print "Hello, NAME!".
def myfunction_with_name(name):
    print("Hello, {}!".format(name))

# Call the modified function with a specific name.
myfunction_with_name("Deniz")


# another example:

def myfunction():
  print("Hello, world!")

myfunction()


def myfunction(name):
  print("Hello,", name, "!")

myfunction("Deniz")
