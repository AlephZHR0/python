from os import system
from art import logo
biders_list = {}

def clean_function():
    system("cls")

def take_the_bid():
    name = str(input("What's your name?\n"))
    bid = float(input("what's your bid?\n$"))
    biders_list[name] = bid

def get_highest_bid():
    highest_bid_value = 0
    for name in biders_list:
        if biders_list[name] > highest_bid_value:
            highest_bid_name = name.capitalize()
            highest_bid_value = biders_list[name]
    return highest_bid_name, highest_bid_value

def main():
    print(logo)
    print("welcome to the secret auction program.")
    biders = 1
    while biders != 0:
        take_the_bid()
        any_bidders = input("Are there any other bidders? Type 'Yes' or 'no'.\n").lower()
        if any_bidders == "yes":
            biders += 1
            clean_function()
        biders -= 1
    highest_bid_name, highest_bid_value = get_highest_bid()
    print("the winner is {} with a bid of ${} ".format(highest_bid_name, highest_bid_value))

main()