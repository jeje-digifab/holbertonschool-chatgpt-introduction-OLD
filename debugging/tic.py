#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check horizontal and vertical lines
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    # Check for tie
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        print("It's a tie!")
        return True
    return False


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    winner = None
    while not check_winner(board):
        print_board(board)
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == " ":
                        board[row][col] = player
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        player = "O" if player == "X" else "X"

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)  # Print the board before returning in case of a tie
            print("It's a tie!")
            return  # Game ends here if it's a tie

    print_board(board)
    winner = "X" if player == "O" else "O"
    print("Player " + winner + " wins!")


tic_tac_toe()
