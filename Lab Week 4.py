import random

def updatedText(kata_rahasia, display_text, guess):
  updated_text = ""
  for i in range (len(kata_rahasia)):
    if kata_rahasia[i].lower() == guess.lower():
      updated_text += guess.lower()
    else:
      updated_text += display_text[i]
  return updated_text

def hangman(kata_rahasia):
  Guesses = []
  chance = 6
  display_text = "_" * len(kata_rahasia)
  print("Welcome to hangman!")
  print("Try to guess the word.")
  print(display_text)

  while kata_rahasia != '' and chance > 0:
    guess = input("Input a letter:").lower()
    if len(guess) != 1:
      print("You have entered more than one word. Please try again!")
    elif not guess.isalpha():
      print("Please input a letter!")
    elif guess.lower() in Guesses:
      print("You have input that letter.")
    else:
      Guesses += guess.lower()

      if guess.lower() in kata_rahasia.lower():
        print("Congrats you guessed a letter!")
        display_text = updatedText(kata_rahasia, display_text, guess)
        print(display_text)
      else:
        chance -= 1
        print("You have failed to guess a letter. You have {} chances left ".format(chance))
        print(display_text)

    if "_" not in display_text:
      print("Congratulations! You have guessed the word:", kata_rahasia)
      playagain()
  
  if chance == 0:
    print("You are out of chances.")
    playagain()

def pemilihan_kata():
  kata_rahasiaku =["Samuel", "abis", "beli"]
  random_word = random.choice(kata_rahasiaku)
  kata_rahasiaku.remove(random_word)
  if len(kata_rahasiaku) == 0: 
    print("You have completed the game. Thank you!")
  return random_word

def playagain():
  user_input = input("Would you like to play again? Yes or No: ").lower()
  if user_input == "yes":
    hangman(pemilihan_kata())
  else:
    print("Thank you for playing. See you next time")

hangman(pemilihan_kata())