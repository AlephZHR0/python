from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.move_distance = 10
        self.penup()
        self.starting_position()

    def move_on(self):
        self.forward(self.move_distance)

    def starting_position(self):
        self.goto(STARTING_POSITION)
