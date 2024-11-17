def display_board(board):
    """Display the Tic Tac Toe board."""
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")

def check_win(board):
    """Check if there is a winner."""
    # rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def play():
    """The main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for turn in range(9):
        display_board(board)
        move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        row, col = divmod(move, 3)
        
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Position already taken! Try again.")
            continue

        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    print("It's a tie!")

# Start the game
if __name__ == "__main__":
    play()
