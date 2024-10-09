import string
from random import choice
length = 64
printables_list = list(string.printable)
for _ in range(5):
    printables_list.pop()
password = ""
for _ in range(length):
    password+= choice(printables_list)
print(password)