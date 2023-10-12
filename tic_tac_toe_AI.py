import random

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def check_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to get empty cells
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax function to determine the best move for the AI
def minimax(board, depth, maximizing_player):
    if check_win(board, 'X'):
        return -10 + depth
    elif check_win(board, 'O'):
        return 10 - depth
    elif check_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

# AI's move using Minimax algorithm
def ai_move(board):
    best_move = None
    best_eval = float('-inf')

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        eval = minimax(board, 0, False)
        board[i][j] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)

    return best_move

# Main function to run the game
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")

    while True:
        display_board(board)

        # Player's move
        while True:
            try:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        # Check if the player wins
        if check_win(board, 'X'):
            display_board(board)
            print("You win!")
            break

        # Check if the board is full (draw)
        if check_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        # AI's move
        row, col = ai_move(board)
        board[row][col] = 'O'

        # Check if the AI wins
        if check_win(board, 'O'):
            display_board(board)
            print("AI wins!")
            break

if __name__ == "__main__":
    main()
