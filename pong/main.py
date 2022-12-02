# TODO 1: Create a screen 800 * 600, black bg color, should stay onscreen until clicked

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")

screen.bgcolor("black")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
score_1 = Scoreboard((20, 250))
score_2 = Scoreboard((-20, 250))

# paddle_1.add_paddle((350, 0))
# paddle_2.add_paddle((-350, 0))

# screen.update()
screen.listen()
screen.onkey(paddle_1.paddle_up, "Up")
screen.onkey(paddle_1.paddle_down, "Down")
screen.onkey(paddle_2.paddle_up, "w")
screen.onkey(paddle_2.paddle_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball bounce
        ball.bounce_y()

    #Detect ball bounce off the paddle
    if ball.xcor() > 320 and ball.distance(paddle_1) < 50:
        ball.bounce_x()
        ball.increase_speed()
    elif ball.xcor() < -320 and ball.distance(paddle_2) < 50:
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 400:
        score_2.score_increase()
        ball.reset()
        ball.bounce_x()

    if ball.xcor() < -400:
        score_1.score_increase()
        ball.reset()
        ball.bounce_x()

    # if score_1 == 10 or score_2


screen.exitonclick()
