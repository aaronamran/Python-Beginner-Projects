import random

print("Let's play a game of Tic-Tac-Toe!\n")


# Create the board
def print_board(board):
    for i in range(0, len(board), 3):
        row = board[i:i + 3]
        print(" | ".join(row))
        if i < 6:
            print("-" * 9)


# Check if a player has won
def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                      (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[
                cond[0]] != " ":
            return True
    return False


# Check if the board is full
def check_draw(board):
    return " " not in board


# Get the player's move
def make_move(board, player, position):
    if board[position] == " ":
        board[position] = player
        return True
    return False


# Get the computer's move
def computer_move(board):
    empty_positions = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(empty_positions)
    board[move] = "O"


# Main game loop
def main():
    board = [" " for _ in range(9)]
    player1 = "X"
    player2 = "O"
    current_player = player1

    while True:
        print_board(board)
        if current_player == player1:
            try:
                move = int(
                    input(f"\nPlayer {current_player}, enter your move (1-9): "
                          )) - 1
                if move < 0 or move > 8:
                    print(
                        "\nInvalid move. Please enter a number between 1 and 9."
                    )
                    continue
                if not make_move(board, current_player, move):
                    print("\nThis position is already taken. Try another one.")
                    continue
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                continue
        else:
            computer_move(board)
            print(f"\nComputer ({player2}) made a move.\n")

        if check_win(board):
            print_board(board)
            if current_player == player1:
                print(f"\nPlayer {current_player} wins!")
            else:
                print("\nComputer wins!")
            break

        if check_draw(board):
            print_board(board)
            print("\nThe game is a draw!")
            break

        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    main()
