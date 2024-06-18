def display_board(board):
  """Displays the current state of the tic-tac-toe board."""
  print("_________ ")
  print(f"{board[0]} | {board[1]} | {board[2]} ")
  print("---------")
  print(f"{board[3]} | {board[4]} | {board[5]} ")
  print("---------")
  print(f"{board[6]} | {board[7]} | {board[8]} ")
  print("_________ ")

def is_valid_move(board, position):
  return board[position] == " "

def make_move(board, player, position):
  board[position] = player

def has_won(board, player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
  for row in win_conditions:
    if all(board[i] == player for i in row):
      return True
  return False

def is_board_full(board):
  """Checks if all positions on the board are filled."""
  return not any(cell == " " for cell in board)

def main():
  """Runs the tic-tac-toe game."""
  player1_name = input("Enter Player 1 name (X): ")
  player2_name = input("Enter Player 2 name (O): ")

  board = [" "] * 9 

  current_player = player1_name
  game_over = False

  while not game_over:
    display_board(board)

  
    while True:
      try:
        position = int(input(f"{current_player}'s turn (enter position 1-9): ")) - 1
        if 0 <= position <= 8 and is_valid_move(board, position):
          break
        else:
          print("Invalid move. Please choose an empty position (1-9).")
      except ValueError:
        print("Invalid input. Please enter a number.")

    make_move(board, current_player[0], position)

    if has_won(board, current_player[0]):
      game_over = True
      print(f"{current_player} wins!")
    elif is_board_full(board):
      game_over = True
      print("It's a tie!")

    current_player = player2_name if current_player == player1_name else player1_name

  display_board(board)
  print("Thanks for playing!")

if __name__ == "__main__":
  main()
