# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_work = 90 - int(age)
d = age_work * 365
w = age_work * 52
m = age_work * 12
print("You have {} days, {} weeks, and {} months left.".format(d, w, m))