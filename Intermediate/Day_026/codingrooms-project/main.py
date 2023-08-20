with open("file1.txt") as file_1:
    first_list = file_1.readlines()

with open("file2.txt") as file_2:
    second_list = file_2.readlines()

result = [int(number) for number in first_list if number in second_list]

# Write your code above 👆

print(result)
