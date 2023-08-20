from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
l_score = Score(-22)
r_score = Score(22)

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330 or ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        ball.increment_speed()
    elif ball.distance(l_paddle) > 50 and ball.xcor() < -330:
        r_score.add_points()
        ball.restart()
    elif ball.distance(r_paddle) > 50 and ball.xcor() > 330:
        l_score.add_points()
        ball.restart()
screen.exitonclick()
