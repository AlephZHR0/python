from turtle import Turtle


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.punctuation = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position, 200)
        self.scoreboard()

    def add_points(self):
        self.punctuation += 1
        self.clear()
        self.scoreboard()

    def scoreboard(self):
        self.write("{}".format(self.punctuation), False, "center", ('Arial', 20, 'normal'))
