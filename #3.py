# import time

# def display_text(text):
#   """Prints the challenge text with a slight delay for better readability."""
#   for char in text:
#     print(char, end='', flush=True)
#     time.sleep(0.05)  # Adjust delay for desired speed

# def get_user_input():
#   """Gets the user's typed input."""
#   user_input = input("\nType the text and press Enter: ")
#   return user_input.strip()

# def calculate_score(original_text, user_text):
#   """Calculates the accuracy score based on correct characters."""
#   correct_chars = 0
#   for i in range(len(original_text)):
#     if original_text[i] == user_text[i]:
#       correct_chars += 1
#   accuracy = (correct_chars / len(original_text)) * 100
#   return accuracy

# def main():
#   """Runs the typing challenge program."""
#   challenge_text = "This is the text you need to type accurately and quickly!"
#   start_time = time.time()

#   display_text(challenge_text)
#   user_input = get_user_input()

#   end_time = time.time()
#   elapsed_time = end_time - start_time

#   accuracy = calculate_score(challenge_text, user_input)

#   print(f"\nYour accuracy: {accuracy:.2f}%")
#   print(f"Time taken: {elapsed_time:.2f} seconds")

# if __name__ == "__main__":
#   main()

import time

def typing_challenge():
  # Define the text to be typed
  text = "This is the text you need to type."

  # Clear the console (optional)
  print("\033c")  # This might not work on all environments

  # Display the text and start timer
  print(text)
  start_time = time.time()

  # Get user input
  user_input = input("Type the text: ")

  # Calculate time taken
  end_time = time.time()
  time_taken = end_time - start_time

  # Calculate accuracy
  correct_chars = 0
  if len(text) >= len(user_input):
    for i in range(len(user_input)):
      if text[i] == user_input[i]:
        correct_chars += 1
    accuracy = (correct_chars / len(text)) * 100
  else:
    for i in range(len(text)):
      if text[i] == user_input[i]:
        correct_chars += 1
    accuracy = (correct_chars / len(user_input)) * 100

  
  print(correct_chars)

  # Display results
  print(f"\nYou typed: {user_input}")
  print(f"Time taken: {time_taken:.2f} seconds")
  print(f"Accuracy: {accuracy:.2f}%")

# Run the challenge
typing_challenge()

