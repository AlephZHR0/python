from turtle import Turtle, Screen
from random import randrange

turtle = Turtle()
screen = Screen()
screen.colormode(255)


def get_random_color():
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_forms():
    for form in range(3, 11):
        turtle.pencolor(get_random_color())
        get_random_color()
        angle = 360 / form
        for i in range(0, form):
            turtle.left(angle)
            turtle.forward(100)


draw_forms()

screen.exitonclick()
