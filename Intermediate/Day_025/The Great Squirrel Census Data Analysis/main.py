import numpy as np
import pandas


class Squirrel:

    def __init__(self):
        self.color = None
        self.amount = 0


squirrel_db = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

list_of_squirrels_colors = []

for color in squirrel_db["Primary Fur Color"]:
    if color not in list_of_squirrels_colors:
        list_of_squirrels_colors.append(color)

list_of_squirrels = []

for color in list_of_squirrels_colors:
    new_squirrel = Squirrel()
    data = squirrel_db[squirrel_db["Primary Fur Color"] == color]
    new_squirrel.color = color
    new_squirrel.amount = len(data)
    list_of_squirrels.append(new_squirrel)

squirrel_colors = []
squirrel_amounts = []

for squirrel in list_of_squirrels:
    squirrel_colors.append(squirrel.color)
    squirrel_amounts.append(squirrel.amount)

squirrel_dict = {
    "Fur Color": squirrel_colors,
    "Count": squirrel_amounts
}
print(squirrel_dict)

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")
