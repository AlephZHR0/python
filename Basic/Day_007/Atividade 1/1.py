#Step 1 

word_list = ["aardvark", "baboon", "camel"]


from random import choice
chosen_word = choice(word_list)
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")