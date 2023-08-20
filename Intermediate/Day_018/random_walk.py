from turtle import Turtle, Screen
from random import choice

angles = [0, 90, 180, 270]
turtle = Turtle()
screen = Screen()
turtle.pensize(5)
turtle.speed(100)


def random_walk(num_of_steps):
    for _ in range(num_of_steps):
        turtle.color(choice(colours))
        turtle.forward(50)
        turtle.setheading(choice(angles))


random_walk(100)

screen.exitonclick()
