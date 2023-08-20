from random import randint, choice
from extras import logo, congratulations_messages

attempts = 0


def dificulty_level():
    global attempts
    dificulty = input("Choose a dificulty. type 'easy' or 'hard': ").lower()
    if dificulty == "easy":
        attempts = 10
    elif dificulty == "hard":
        attempts = 5
    else:
        print("wrong input")
        dificulty_level()


def main_game(correct_answer, attempts):
    guess = -1
    while guess != correct_answer and attempts != 0:
        print("You have {} attempts remaining to guess the number.".format(attempts))
        guess = (input("Make a guess: "))
        if guess.isnumeric():
            guess = int(guess)
            if guess == correct_answer:
                print(choice(congratulations_messages))
            else:
                if guess > correct_answer:
                    print("too low buddy")
                elif guess < correct_answer:
                    print("too high buddy")
                attempts -= 1
        else:
            print("Wrong input, please try again")
            main_game(correct_answer, attempts)


def again():
    want_to_play_again = input("want to play again? 'Y' or 'N': ").lower()
    if want_to_play_again == "y":
        main()
    elif want_to_play_again == "n":
        return
    else:
        print("Wrong input, please try again")
        again()


def main():
    print(f"{logo}\n\nWelcome to the Number Guessing game!")
    correct_answer = randint(1, 100)
    print("I'm thinking of a number between 1 and 100")
    main_game(correct_answer, dificulty_level())
    again()


main()
