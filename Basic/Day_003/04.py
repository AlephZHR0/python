# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("Welcome to Python Pizza Deliveries!")
Size = input("What size pizza do you want? S, M or L ")
Peperoni = input("Do you want peperoni? Y or N")
Cheese = input("Do you want extra cheese? Y or N")

if Size == "S":
    total_tamanho = 15
elif Size == "M":
    total_tamanho = 20
else:
    total_tamanho = 25
if Peperoni == "Y" and Size == "S":
    total_peperoni = 2
elif Peperoni == "Y" and Size == "M" or "L":
    total_peperoni = 3
else:
    total_peperoni = 0
if Cheese == "Y":
    total_cheese = 1
else:
    total_cheese = 0
total = total_tamanho + total_peperoni + total_cheese
print("Your final bill is: ${}.".format(total))