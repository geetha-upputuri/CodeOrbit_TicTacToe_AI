import random

# Define the players
HUMAN = "X"
COMPUTER = "O"
EMPTY = " "

# All possible winning combinations
WINNING_COMBINATIONS = [
    (0, 1, 2),  # First row
    (3, 4, 5),  # Second row
    (6, 7, 8),  # Third row
    (0, 3, 6),  # First column
    (1, 4, 7),  # Second column
    (2, 5, 8),  # Third column
    (0, 4, 8),  # Main diagonal
    (2, 4, 6)   # Other diagonal
]


def display_board(board):
    """Display the Tic-Tac-Toe board."""

    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    """Check whether the given player has won."""

    for combination in WINNING_COMBINATIONS:
        a, b, c = combination

        if (
            board[a] == player
            and board[b] == player
            and board[c] == player
        ):
            return True

    return False


def is_draw(board):
    """Check whether the game is a draw."""

    return EMPTY not in board


def get_human_move(board):
    """Get a valid move from the human player."""

    while True:
        try:
            position = int(
                input("Enter your position (1-9): ")
            )

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")

            elif board[position - 1] != EMPTY:
                print("That position is already occupied.")

            else:
                return position - 1

        except ValueError:
            print("Invalid input. Enter a number.")


def find_winning_move(board, player):
    """Find a move that allows the player to win."""

    for position in range(9):

        if board[position] == EMPTY:

            # Temporarily place the player's mark
            board[position] = player

            # Check whether this move creates a win
            if check_winner(board, player):
                board[position] = EMPTY
                return position

            # Undo the temporary move
            board[position] = EMPTY

    return None


def get_computer_move(board):
    """Choose an intelligent move for the computer."""

    # Rule 1: Win immediately if possible
    winning_move = find_winning_move(board, COMPUTER)

    if winning_move is not None:
        print("AI chooses a winning move!")
        return winning_move

    # Rule 2: Block the human from winning
    blocking_move = find_winning_move(board, HUMAN)

    if blocking_move is not None:
        print("AI blocks your winning move!")
        return blocking_move

    # Rule 3: Choose the center
    if board[4] == EMPTY:
        print("AI chooses the center.")
        return 4

    # Rule 4: Choose an available corner
    corners = [0, 2, 6, 8]

    available_corners = [
        position
        for position in corners
        if board[position] == EMPTY
    ]

    if available_corners:
        print("AI chooses a corner.")
        return random.choice(available_corners)

    # Rule 5: Choose any remaining position
    available_positions = [
        position
        for position in range(9)
        if board[position] == EMPTY
    ]

    print("AI chooses an available position.")

    return random.choice(available_positions)


def play_game():
    """Run one complete game."""

    board = [EMPTY] * 9

    print("\nWelcome to Tic-Tac-Toe AI!")
    print("You are X. The computer is O.")

    # Display the position guide
    print("\nPosition Guide:")
    display_board(["1", "2", "3", "4", "5",
                   "6", "7", "8", "9"])

    while True:

        # Human player's turn
        human_move = get_human_move(board)
        board[human_move] = HUMAN

        display_board(board)

        # Check whether the human has won
        if check_winner(board, HUMAN):
            print("Congratulations! You win!")
            break

        # Check whether the game is a draw
        if is_draw(board):
            print("The game is a draw!")
            break

        # Computer's turn
        computer_move = get_computer_move(board)
        board[computer_move] = COMPUTER

        print(
            f"Computer places O at position "
            f"{computer_move + 1}."
        )

        display_board(board)

        # Check whether the computer has won
        if check_winner(board, COMPUTER):
            print("Computer wins! Better luck next time.")
            break

        # Check whether the game is a draw
        if is_draw(board):
            print("The game is a draw!")
            break


def main():
    """Start and manage the game."""

    while True:

        play_game()

        replay = input(
            "\nDo you want to play again? (yes/no): "
        ).strip().lower()

        if replay not in ("yes", "y"):
            print("Thank you for playing Tic-Tac-Toe AI!")
            break


# Execute the program
if __name__ == "__main__":
    main()
