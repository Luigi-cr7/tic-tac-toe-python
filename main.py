def create_board():
    return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def player_input(player, board):
    while True:
        move = input(f"Player {player}, enter your move (1-9) or type 'exit' to quit: ").strip()
        if move.lower() == "exit":
            return "exit"
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9 and board[move - 1] not in ["X", "O"]:
                return move - 1
            else:
                print("Invalid move. That spot is already taken or out of range.")
        else:
            print("Invalid input. Please enter a number between 1 and 9, or 'exit'.")

def update_board(board, move, player):
    board[move] = player

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(cell in ["X", "O"] for cell in board)

def switch_player(player):
    return "O" if player == "X" else "X"

def play_game():
    print("Welcome to Tic Tac Toe!")
    while True:
        board = create_board()
        current_player = "X"
        print_board(board)

        while True:
            move = player_input(current_player, board)
            if move == "exit":
                print("Game exited.")
                return
            update_board(board, move, current_player)
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            if is_draw(board):
                print("It's a draw!")
                break

            current_player = switch_player(current_player)

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
play_game()
