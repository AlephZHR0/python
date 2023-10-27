import string
import pyperclip
from random import choice

length = int(input('Enter the length of the password: '))
PRINTABLES_LIST = list(string.printable)
for _ in range(5):
    PRINTABLES_LIST.pop()
password = ''
for _ in range(length):
    password += choice(PRINTABLES_LIST)
pyperclip.copy(password)
print('Password was copied to clipboard.')
