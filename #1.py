import random

secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")

guesses = 0

while True:
  guesses += 1

  try:
    guess = int(input("Enter your guess (1-100): "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue


  if guess < 1 or guess > 100:
    print("Guess must be between 1 and 100.")
    continue


  if guess == secret_number:
    print(f"Congratulations! You guessed the number in {guesses} attempts.")
    break
  elif guess < secret_number:
    print("Too low, try again.")
  else:
    print("Too high, try again.")

print("Thanks for playing!")
