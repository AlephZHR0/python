#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


list_of_letters = []
list_of_numbers = []
list_of_symbols = []
for i in range(0, nr_letters):
    list_of_letters += random.choice(letters)
for i in range(0, nr_numbers):
    list_of_numbers += random.choice(numbers)
for i in range(0, nr_symbols):
    list_of_symbols += random.choice(symbols)
password = list_of_letters + list_of_numbers + list_of_symbols

ez_password = ""
for i in password:
    ez_password += i

print("Here is your ez password: {}".format(ez_password))

random.shuffle(password)
hard_password = ""
for i in password:
    hard_password += i

print("Here is your hard password: {}".format(hard_password))