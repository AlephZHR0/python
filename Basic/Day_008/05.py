alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(plain_text, shift_amount):
    new_text = ""
    for i in range(len(plain_text)):
        new_letter = alphabet[(alphabet.index(plain_text[i]) + shift_amount) % 26]
        new_text += new_letter
    print("The encoded text is {}".format(new_text))
def decrypt(plain_text, shift_amount):
    new_text = ""
    for i in range(len(plain_text)):
        new_letter = alphabet[(alphabet.index(plain_text[i]) - shift_amount) % 26]
        new_text += new_letter
    print("The decoded text is {}".format(new_text))

  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


def main():
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if choice == "encode":
        encrypt(text, shift)
    elif choice == "decode":
        decrypt(text, shift)
    else:
        print("Before trying to encrypt or decrypt, try learning ENGLISH!")

main()