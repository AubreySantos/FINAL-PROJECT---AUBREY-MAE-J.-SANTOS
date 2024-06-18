def convert_mm_to_cm(value):
  """Converts millimeters (mm) to centimeters (cm)."""
  return value / 10

def convert_cm_to_mm(value):
  """Converts centimeters (cm) to millimeters (mm)."""
  return value * 10

def convert_ft_to_m(value):
  """Converts feet (ft) to meters (m)."""
  return value * 0.3048

def convert_m_to_ft(value):
  """Converts meters (m) to feet (ft)."""
  return value / 0.3048

def convert_kg_to_g(value):
  """Converts kilograms (kg) to grams (g)."""
  return value * 1000

def convert_g_to_kg(value):
  """Converts grams (g) to kilograms (kg)."""
  return value / 1000

def display_menu():
  """Prints the menu options for unit conversion."""
  print("\nMeasurement Converter Menu:")
  print("1. Millimeters (mm) to Centimeters (cm)")
  print("2. Centimeters (cm) to Millimeters (mm)")
  print("3. Feet (ft) to Meters (m)")
  print("4. Meters (m) to Feet (ft)")
  print("5. Kilograms (kg) to Grams (g)")
  print("6. Grams (g) to Kilograms (kg)")
  print("7. Exit")

def get_user_choice():
  """Gets the user's choice from the menu."""
  while True:
    try:
      choice = int(input("\nEnter your choice (1-7): "))
      if 1 <= choice <= 7:
        return choice
      else:
        print("Invalid choice. Please enter a number between 1 and 7.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_user_input(message):
  """Gets a numerical input from the user with a prompt message."""
  while True:
    try:
      value = float(input(message))
      return value
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  """Runs the main program loop for the measurement converter."""
  while True:
    display_menu()
    choice = get_user_choice()

    if choice == 7:
      print("Exiting the converter. Thank you!")
      break

    value = get_user_input("Enter the value to convert: ")

    if choice == 1:
      converted_value = convert_mm_to_cm(value)
      print(f"{value} mm is equal to {converted_value:.2f} cm")
    elif choice == 2:
      converted_value = convert_cm_to_mm(value)
      print(f"{value} cm is equal to {converted_value:.2f} mm")
    elif choice == 3:
      converted_value = convert_ft_to_m(value)
      print(f"{value} ft is equal to {converted_value:.2f} m")
    elif choice == 4:
      converted_value = convert_m_to_ft(value)
      print(f"{value} m is equal to {converted_value:.2f} ft")
    elif choice == 5:
      converted_value = convert_kg_to_g(value)
      print(f"{value} kg is equal to {converted_value:.2f} g")
    elif choice == 6:
      converted_value = convert_g_to_kg(value)
      print(f"{value} g is equal to {converted_value:.2f} kg")

if __name__ == "__main__":
  main()
