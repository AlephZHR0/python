from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

DIMENSIONS = 600

# Setup
screen = Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.setup(DIMENSIONS, DIMENSIONS)
screen.bgcolor("black")
# Importing classes
snake = Snake()
food = Food()
scoreboard = Scoreboard(DIMENSIONS)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
# Game
game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.SNAKE_HEAD.distance(food) < 15:
        scoreboard.add_points()
        food.refresh_location()
        snake.add_snake_part()
    if snake.SNAKE_HEAD.xcor() > ((DIMENSIONS / 2) - 20)\
        or snake.SNAKE_HEAD.xcor() < -(DIMENSIONS / 2)\
        or snake.SNAKE_HEAD.ycor() > (DIMENSIONS / 2)\
        or snake.SNAKE_HEAD.ycor() < -((DIMENSIONS / 2) - 20):
        scoreboard.game_over()
        game_on = False
    for segment in snake.SNAKE_PARTS[1:]:
        if snake.SNAKE_HEAD.distance(segment) < 10:
            game_on = False
screen.exitonclick()
