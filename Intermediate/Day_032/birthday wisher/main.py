from datetime import datetime
from random import randint
import pandas
##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
with open("birthdays.csv") as bithday_file:
    data = pandas.read_csv(bithday_file)
    birth_date = data[data.day == now.day].day.item()
    name = data[data.day == now.day].name.item()
    
if now.day == birth_date:
    
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open("letter_templates\letter_{}.txt".format(randint(1,3))) as letter:
        all_letter = letter.read()
        all_letter = all_letter.replace("[NAME]", name)
        print(all_letter)


# 4. Send the letter generated in step 3 to that person's email address.




