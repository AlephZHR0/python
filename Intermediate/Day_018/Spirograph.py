from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.speed("fastest")
angle = 0


def spirograph(num_of_circles):
    for i in range(0, num_of_circles):
        turtle.left(360 / num_of_circles)
        turtle.circle(100)


spirograph(4)

screen.exitonclick()
