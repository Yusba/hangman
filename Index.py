import random
from hangman_words import word_list
from hangman_art import logo

end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(('Crunk Colony', 'bold'))



print(logo)
print("\n")
print(('Some Names of people on Crunk colony', 'bold'))
print("\n")
print('Psssst, the solution is')
print((f'"{chosen_word}"', ))

print("\n")

display = []

for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a Letter: ").lower()


  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:

    print(f"You guessed {guess},thats not in the word.You lose a life")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You Win.")
  from hangman_art import stages
  print(stages[lives])
