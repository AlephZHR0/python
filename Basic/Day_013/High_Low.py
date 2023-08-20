from art import logo, vs
from game_data import data
from random import choice

wrong_answer = False


def get_character():
    return choice(data)


def get_answer(f_char, s_char):
    p_char = 0
    other = 0
    p_ans = input("Who has more followers? Type 'A', or 'B': ").lower()
    if p_ans == 'a':
        p_char = f_char["follower_count"]
        other = s_char["follower_count"]
    elif p_ans == 'b':
        p_char = s_char["follower_count"]
        other = f_char["follower_count"]
    else:
        print("Invalid choice, please, try again")
        get_answer(f_char, s_char)
    return p_char, other


def check_answer(p_char, other):
    global wrong_answer

    if p_char > other:
        print("Nice one!")
        main_game()
    else:
        wrong_answer = True


def prints_funct(score, f_char, s_char):
    print(logo)
    print("Your current score is: {}".format(score))
    print("compare A: {}, a {}, from {}".format(
        f_char["name"],
        f_char["description"],
        f_char["country"]
    ))
    print(vs)
    print("Against B: {}, a {}, from {}".format(
        s_char["name"],
        s_char["description"],
        s_char["country"]
    ))


def first_game_run(score):
    f_char = get_character()
    s_char = get_character()
    prints_funct(score, f_char, s_char)
    char_1, char_2 = get_answer(f_char, s_char)
    check_answer(char_1, char_2)
    return f_char, s_char


def main_game(score, f_char, s_char):
    f_char = s_char
    s_char = get_character()
    prints_funct(f_char, s_char)
    get_answer(f_char, s_char)


def main():
    global wrong_answer
    score = 0
    f_char, s_char = first_game_run(score)
    while wrong_answer:
        main_game(score, f_char, s_char)
    play_again = input("You lost, want to try again?").lower()
    if play_again == 'y':
        wrong_answer = False
        main()
    elif play_again == 'n':
        print("Thanks for playing")
        return


main()