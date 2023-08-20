from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def forwards():
    turtle.forward(10)


def backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear_screen():
    turtle.clear()
    screen.resetscreen()

screen.listen()
screen.onkeypress(forwards, "w")
screen.onkeypress(backwards, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear_screen, "c")

screen.exitonclick()
