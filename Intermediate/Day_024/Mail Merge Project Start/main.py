# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


list_of_names = []

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        list_of_names.append(name.strip())

with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in list_of_names:
        new_letter = letter_content.replace("[name]", name)
        with open("Output/ReadyToSend/letter_for_{}.txt".format(name), "w") as letter_for:
            letter_for.write(new_letter)
