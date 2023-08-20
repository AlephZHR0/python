#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

for i in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
        print("Right")
        display[letter] = guess
    else:
        print("Wrong")
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)