import random

from hangman_art import logo, stages
print(logo)

from hangman_words import word_list
chosen_word = random.choice(word_list)

display = []
for n in chosen_word:
    display += "_"

lives = 6
print(stages[lives])

finished = False
while not finished:  
  guess = input("Guess a letter: ").lower()
  
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      if letter in display:
        print(f"You've already guessed {guess}")
      else:
        display[position] = guess
    
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
      finished = True
      print("\nYOU LOSE!\n")
      print(f"Answer: {chosen_word}")

  if "_" not in display:
    finished = True
    print("\nYOU WIN!\n")

  print(f"{' '.join(display)}")
  print(stages[lives])