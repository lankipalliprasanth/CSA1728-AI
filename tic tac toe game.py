def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print("Welcome to Tic Tac Toe!")
    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, choose a row (0-2): "))
        col = int(input(f"Player {players[current_player]}, choose a column (0-2): "))
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = players[current_player]
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 1 - current_player
if __name__ == "__main__":
    play_game()
