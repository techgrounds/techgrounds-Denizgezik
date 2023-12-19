# Use a while loop to repeat the game until the user inputs 100.
while True:
    # Ask the user for a number.
    user_number = int(input("Please input a number: "))

    # Give a response based on the user's number.
    if user_number < 100:
        print("{} is pretty low, isn't it?".format(user_number))
    elif user_number > 100:
        print("Wow, {} is a big number!".format(user_number))
    else:
        print("{} is a nice number indeed.".format(user_number))
        break  # Exit the loop if the user inputs 100


# Second example:

while True:
    number = int(input("Please input a number: "))
    if number < 100:
        print(f"{number} Oh no, my dear, isn't that a bit too low? ⬇️")
    elif number > 100:
        print(f"Wow, {number}! Now, take it easy, Champ. That's quite a big number! ⬆️")
    else:
        print("You guessed it right, Master! 🎉")
        break
