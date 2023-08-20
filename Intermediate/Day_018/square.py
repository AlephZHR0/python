from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def square(size, line_type):
    for i in range(0, 4):
        turtle.forward(size)
        turtle.left(90)

square(100)

screen.exitonclick()
