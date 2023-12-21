import random

def is_valid_move(move):
    """Check if the player's move is valid."""
    valid_moves = ["rock", "paper", "scissors", "r", "p", "s"]
    return move.lower() in valid_moves

def generate_computer_move():
    """Generate a random move for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_move, computer_move):
    """Determine the winner of the round."""
    if player_move == computer_move:
        return "It's a tie!"
    elif (
        (player_move == "rock" and computer_move == "scissors") or
        (player_move == "paper" and computer_move == "rock") or
        (player_move == "scissors" and computer_move == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_round():
    """Play a single round of Rock, Paper, Scissors."""
    player_move = input("Enter your move (rock, paper, scissors): ")
    
    # Check if the player's move is valid
    while not is_valid_move(player_move):
        print("Invalid move. Please enter a valid move.")
        player_move = input("Enter your move (rock, paper, scissors): ")

    # Generate the computer's move
    computer_move = generate_computer_move()

    print("Computer's move:", computer_move)

    # Determine the winner of the round and print the result
    result = determine_winner(player_move.lower(), computer_move)
    print(result)

    return result

def play_game(num_rounds):
    """Play the Rock, Paper, Scissors game for a specified number of rounds."""
    player_score = 0
    computer_score = 0

    for _ in range(num_rounds):
        print("\nRound {}: ".format(_ + 1))
        result = play_round()

        # Update scores
        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

    # Print the final scores
    print("\nGame Over! Final Scores:")
    print("Player: {}".format(player_score))
    print("Computer: {}".format(computer_score))

if __name__ == "__main__":
    # Play the game for a predetermined number of rounds (e.g., 3 rounds)
    play_game(3)
