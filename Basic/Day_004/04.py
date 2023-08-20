rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import choice
elements = [rock, paper, scissors]
choosen_game = choice(elements)
choosen_guy = input("Choose between 'Rock', 'Paper', 'Scissors'.").lower()

if choosen_guy == 'rock':
    print(rock)
    if choosen_game == rock:
        print(rock)
        print("Tie")
    elif choosen_game == paper:
        print(paper)
        print("The PC won")
    elif choosen_game == scissors:
        print(scissors)
        print("You won")

elif choosen_guy == "paper":
    print(paper)
    if choosen_game == rock:
        print(rock)
        print("You won")
    elif choosen_game == paper:
        print(paper)
        print("Tie")
    elif choosen_game == scissors:
        print(scissors)
        print("The PC won")
elif choosen_guy == "scissors":
    print(scissors)
    if choosen_game == rock:
        print(rock)
        print("The PC won")
    elif choosen_game == paper:
        print(paper)
        print("You won")
    elif choosen_game == scissors:
        print(scissors)
        print("Tie")
else:
    print("dud, wtf?")
