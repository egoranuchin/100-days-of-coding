import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
score = Scoreboard((-250, 250))
cars = CarManager()

# TODO Gameplay 1: Turtle moves forwards with "up" key. It moves only foward

# TODO Gameplay 3: When the turtle reaches the top of the screen, it resets to the original position and the level ups. The next level has cars with more speed
# TODO Gameplay 4: If the turtle collides with a car, the game overs and everything stops with a "GAME OVER" prompt.

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate()
    cars.move_cars()

    if player.ycor() == 260:
        player.reset_position()
        score.level_increase()
        cars.speed_increase()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()







screen.exitonclick()