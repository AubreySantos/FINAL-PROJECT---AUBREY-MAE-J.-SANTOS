import random

def play_round():
  """Plays a single round of rock-paper-scissors.

  Returns:
      1 if user wins, -1 if computer wins, 0 for tie.
  """
  options = ["rock", "paper", "scissors"]
  user_choice = input("Choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(options)

  if user_choice == computer_choice:
    print("It's a tie!")
    return 0
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    return 1
  else:
    print("You lose!")
    return -1

def main():
  """Runs the best-of-three rock-paper-scissors game."""
  user_score = 0
  computer_score = 0

  while user_score < 2 and computer_score < 2:
    round_result = play_round()
    user_score += round_result
    computer_score -= round_result  # Subtract for computer win

  if user_score == 2:
    print("You win the best-of-three!")
  else:
    print("Computer wins the best-of-three!")

if __name__ == "__main__":
  main()
