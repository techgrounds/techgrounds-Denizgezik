import random

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    """Check if the player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Check if the board is full (a tie)."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_player_move(player):
    """Get the player's move."""
    move = input("Player {}, enter your move (row, column): ".format(player))
    return tuple(map(int, move.split(",")))

def get_computer_move(board):
    """Generate a random move for the computer."""
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_tic_tac_toe():
    """Play a game of Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)  # Randomly determine who starts

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if current_player == "X" or (current_player == "O" and not is_winner(board, "X")):
            row, col = get_player_move(current_player)
        else:
            row, col = get_computer_move(board)
            print("Computer chooses {}, {}".format(row, col))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)

            if is_winner(board, current_player):
                print("Player {} wins!".format(current_player))
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Please try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
