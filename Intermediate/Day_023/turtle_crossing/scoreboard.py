from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.scoreboard()

    def passed_level(self):
        self.level += 1
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write("Level: {}".format(self.level), font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
