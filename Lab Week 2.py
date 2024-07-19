def calculator():
  """
  This function performs basic arithmetic operations (+, -, *, /) on two user-provided numbers.
  """
  # Get numbers from the user
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Get the operation symbol from the user
  operation = input("Choose an operation (+, -, *, /): ")

  # Perform the operation based on the symbol
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    if num2 == 0:  # Handle division by zero error
      print("Error: Division by zero is not allowed.")
      return  # Exit the function if division by zero
    else:
      result = num1 / num2
  else:
    print("Invalid operation symbol. Please use +, -, *, or /.")
    return  # Exit the function if invalid operation symbol

  # Print the result
  print(f"The result of {num1} {operation} {num2} is: {result}")

# Call the calculator function
calculator()

#Hangman
Word = "help"
Guesses = []
chance = 6 

while Word != '' and chance > 0:
  guess = input("Input a letter:").lower()
  if len(guess) != 1:
    print("You have entered more than one word. Please try again!")
  elif guess not in Word:
    chance -= 1
    print("You have failed.")
  elif guess in Word:
    print("Good job, you guessed one letter.")
    Guesses.append
  for letter in Word:
    if letter in Guesses:
      print("Congratulations, you have guessed the word correctly!")
    break

if chance == 0:
    print("you are out of chances")
