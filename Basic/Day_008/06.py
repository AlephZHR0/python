alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(want_to, text, shift_amount):
    if want_to == "decode":
        shift_amount = -shift_amount
    new_text = ""
    for i in range(len(text)):
        new_letter = alphabet[(alphabet.index(text[i]) + shift_amount) % 27]
        new_text += new_letter
    print("The decoded text is {}".format(new_text))

caesar(direction, text, shift)