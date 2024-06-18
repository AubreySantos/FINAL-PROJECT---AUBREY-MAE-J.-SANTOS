import random

def roll_dice():
  """Rolls a single die and returns the random number."""
  return random.randint(1, 6)

def play_round(player_name):
  """Plays a single round for a player.

  Args:
      player_name: The name of the player.

  Returns:
      The player's roll value.
  """
  print(f"\n{player_name}'s turn:")
  input("Press Enter to roll the dice...")
  player_roll = roll_dice()
  print(f"{player_name} rolled: {player_roll}")
  return player_roll

def main():
  """Runs the best-of-three dice-rolling game."""
  player1_name = input("Enter Player 1 name: ")
  player2_name = input("Enter Player 2 name: ")

  player1_score = 0
  player2_score = 0

  for round_number in range(1, 4):
    print(f"\nRound {round_number}")

    player1_roll = play_round(player1_name)
    player2_roll = play_round(player2_name)

    if player1_roll > player2_roll:
      print(f"{player1_name} wins round {round_number}!")
      player1_score += 1
    elif player2_roll > player1_roll:
      print(f"{player2_name} wins round {round_number}!")
      player2_score += 1
    else:
      print("It's a tie!")

    if player1_score == 2 or player2_score == 2:
      break  # Exit loop if one player reaches 2 wins

  if player1_score == 2:
    print(f"\n{player1_name} wins the best-of-three!")
  else:
    print(f"\n{player2_name} wins the best-of-three!")

if __name__ == "__main__":
  main()
