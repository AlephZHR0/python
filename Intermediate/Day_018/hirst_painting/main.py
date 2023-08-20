import colorgram
from turtle import Turtle, Screen
from random import choice

colors = colorgram.extract("LittlePrince.jpg", 100)
list_of_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    list_of_colors.append(rgb)

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.speed(0)


def square_of_circles(size):
    pos_x = 0
    pos_y = 0
    turtle.setx(pos_x)
    turtle.sety(pos_y)
    for i in range(size):
        for _ in range(size):
            turtle.forward(50)
            turtle.dot(20, choice(list_of_colors))
            pos_y += 5
        turtle.setx(0)
        turtle.sety(pos_y)


square_of_circles(10)
screen.exitonclick()
