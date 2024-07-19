Word = "help"
Guesses = []
chance = 6 

while Word != '' and chance > 0:
  guess = input("Input a letter:").lower()
  print(guess)
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

    

      
  




