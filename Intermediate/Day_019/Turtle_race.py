from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []
screen = Screen()
screen_x = 1920
screen_y = 1080
screen.setup(screen_x, screen_y)


def generate_turtles():
    global turtles_list

    space_between_turtles = (screen_y / len(colors))
    pos_y = -(screen_y / 2) + space_between_turtles / 2
    for i in range(0, len(colors)):
        turtle = Turtle("turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.setheading(180)
        turtle.setx(-(screen_x / 2))
        if i > len(colors) / 2:
            turtle.setheading(90)
        elif i == len(colors) / 2:
            turtle.setheading(0)
        elif i < len(colors) / 2:
            turtle.setheading(270)
        turtle.sety(pos_y)
        turtle.setheading(0)
        turtles_list.append(turtle)
        pos_y += space_between_turtles


def run():
    global turtles_list
    i = 0
    for turtle in turtles_list:
        distance = randint(1, 5)
        turtle.forward(distance)


def main():
    user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
    nobody_finished = True
    generate_turtles()
    while nobody_finished:
        for turtle in turtles_list:
            if turtle.xcor() > (screen_x / 2) - 20:
                winner = turtle.pencolor()
                print("The winner is {}".format(winner))
                nobody_finished = False
                if user_bet == winner:
                    print("You won!")
                    break
                else:
                    print("You lost")
                    break
        run()


main()
screen.exitonclick()