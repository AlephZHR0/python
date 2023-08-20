from art import logo, vs
from game_data import data
from random import choice

score = 0
def get_random_character():
    return choice(data)


def prints_function(f_char, s_char):
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


def check_answer(f_char, s_char):
    usr_answer = input("'A' or 'B': ")
    if usr_answer == 'a':
        user = f_char["follower_count"]
        pc = s_char["follower_count"]
    elif usr_answer == 'b':
        user = s_char["follower_count"]
        pc = f_char["follower_count"]
    if user > pc:
        print("Oh yes")
    elif user < pc:
        print("Oh no")


def main_game(is_first, f_char = "", s_char = ""):
    if is_first:
        f_char = get_random_character()
        s_char = get_random_character()
    else:
        f_char = s_char
        s_char = get_random_character()
    prints_function(f_char, s_char)
    check_answer(f_char, s_char)
    return f_char, s_char


def main():
    wrong_answer = False
    f_char, s_char = main_game(True)
    while not wrong_answer:
        f_char, s_char = main_game(False, f_char, s_char)


main()
