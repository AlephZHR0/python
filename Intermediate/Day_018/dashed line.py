from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def dashed_line(repetitions, line_size):
    turtle.color("red")
    for i in range(repetitions):
        turtle.pendown()
        turtle.forward(line_size)
        turtle.penup()
        turtle.forward(line_size)


dashed_line(10, 10)

screen.exitonclick()
