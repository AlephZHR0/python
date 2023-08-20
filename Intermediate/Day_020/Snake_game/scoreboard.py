from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, y_dimension):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.goto(0, (y_dimension / 2) - 35)
        self.refresh_score()

    def add_points(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, "center", ("Arial", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 70, "bold"))
