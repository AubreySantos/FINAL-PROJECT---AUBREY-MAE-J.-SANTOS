import random
import string

def generate_password(length):
  letters = string.ascii_letters
  digits = string.digits
  all_chars = letters + digits
  password = ''.join(random.sample(all_chars, length))

  return password

while True:
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      print("Password length must be at least 8 characters. Please try again.")
    else:
      break
  except ValueError:
    print("Invalid input. Please enter a number.")

password = generate_password(length)
print("Your generated password:", password)
