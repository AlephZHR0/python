from art import logo
from random import choice
from os import system

ALL_CARDS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
INITIAL_NUMBER_OF_CARDS = 2

def new_card(who_receives):
    """Defines a new card to receiver"""
    new_card = choice(ALL_CARDS)
    who_receives.append(new_card)

def initial_hand(user_cards, computer_cards):
    for _ in range(INITIAL_NUMBER_OF_CARDS):
        new_card(user_cards)
        new_card(computer_cards)
    print("Your cards: {} and {}".format(user_cards[0], user_cards[1]))
    print("Computer's first card: {}".format(computer_cards[0]))

def another_card(user_cards):
    while sum_of_hand(user_cards) < 21:
        want_another_card = input("Type 'y' to get another card, type 'n' to pass:\n")
        if want_another_card == "y":
            new_card(user_cards)
            print("Now, your cards are: {}".format(", ".join(user_cards)))
            another_card(user_cards)
        elif want_another_card == "n":
            break
        else:
            print("invalid input, please, type a valid input")
            another_card(user_cards)

def final_hand(user_cards, computer_cards):
    print("your final hand: {}".format(", ".join(user_cards)))
    print("computer's final hand: {}".format(", ".join(computer_cards)))

def sum_of_hand(player_cards):
    player_cards_int = []
    for card in player_cards:
        if card.isnumeric() == True:
            player_cards_int.append(int(card))
        else:
            if card == "A":
                player_cards_int.append(1)
            else:
                player_cards_int.append(10)
    player_total = (sum(player_cards_int))
    return player_total

def winner(user_cards, computer_cards):
    user_total = sum_of_hand(user_cards)
    computer_total = sum_of_hand(computer_cards)
    if user_total > 21:
        print("You lost")
    elif user_total > computer_total:
        print("You won")
    elif user_total == computer_total:
        print("Tie!")
    else:
        print("You lost")

def want_to_play_again():
    keep = input("Want to play again? 'Y' or 'N'\n").lower()
    if keep == "y":
        system("cls")
        main()
    elif keep == "n":
        return
    else:
        print("invalid input, please, type a valid input")
        want_to_play_again()

def main():
    print(logo)
    user_cards = []
    computer_cards = []
    initial_hand(user_cards, computer_cards)
    while sum_of_hand(computer_cards) < 11:
        new_card(computer_cards)
        print("computer pulled out another card!")
    another_card(user_cards)
    final_hand(user_cards, computer_cards)
    winner(user_cards, computer_cards)
    want_to_play_again()

main()