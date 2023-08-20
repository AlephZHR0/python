# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = (name1+name2).lower()

true_score = 0

true_score += names.count("t")
true_score += names.count("r")
true_score += names.count("u")
true_score += names.count("e")

love_score = 0

love_score += names.count("l")
love_score += names.count("o")
love_score += names.count("v")
love_score += names.count("e")

contador = int(str(true_score) + str(love_score))

if contador < 10 or contador > 90:
    print("Your score is {}, you go together like coke and mentos.".format(contador))
elif 40 < contador < 50:
    print("Your score is {}, you are alright together.".format(contador))
else:
    print("Your score is {}.".format(contador))