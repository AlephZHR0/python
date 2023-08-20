from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.SNAKE_PARTS = []
        self.create_snake()
        self.SNAKE_HEAD = self.SNAKE_PARTS[0]

    def create_snake(self):
        temp_x_axis = 0.00
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(temp_x_axis, 0.00)
            self.SNAKE_PARTS.append(snake)
            temp_x_axis -= 20.00
        self.SNAKE_PARTS = self.SNAKE_PARTS

    def add_snake_part(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(self.SNAKE_PARTS[-1].position())
        self.SNAKE_PARTS.append(snake)

    def move(self):
        for i in range((len(self.SNAKE_PARTS) - 1), 0, -1):
            new_x_coordinate = self.SNAKE_PARTS[i - 1].xcor()
            new_y_coordinate = self.SNAKE_PARTS[i - 1].ycor()
            self.SNAKE_PARTS[i].goto(new_x_coordinate, new_y_coordinate)
        self.SNAKE_PARTS[0].forward(20)

    def up(self):
        if self.SNAKE_HEAD.heading() != 270:
            self.SNAKE_HEAD.setheading(UP)

    def down(self):
        if self.SNAKE_HEAD.heading() != 90:
            self.SNAKE_HEAD.setheading(DOWN)

    def left(self):
        if self.SNAKE_HEAD.heading() != 0:
            self.SNAKE_HEAD.setheading(LEFT)

    def right(self):
        if self.SNAKE_HEAD.heading() != 180:
            self.SNAKE_HEAD.setheading(RIGHT)
