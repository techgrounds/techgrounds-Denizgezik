import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize variables
    attempts = 0
    guessed_number = None

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the secret number between 1 and 100.")

    while guessed_number != secret_number:
        # Ask the player to guess a number
        try:
            guessed_number = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guessed_number == secret_number:
            print("Congratulations! You guessed the right number!")
            print("Number of attempts: {}".format(attempts))
        else:
            # Provide a clue for wrong guesses
            if guessed_number < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

if __name__ == "__main__":
    number_guessing_game()
