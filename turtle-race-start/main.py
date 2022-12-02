import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle you think will win the race? Name it's color:")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# turtles = []
# turtle = {"name", "number", "color"}
# last_pos = []

# Naive auto-placer
# for i in range(7):
#     i = Turtle(shape="turtle")
#     i.pu()
#     i.goto(x=-249, y=-100)
#     if int(i.ycor()) == -100:
#         i.goto(x=-249, y=(last_pos[1]-33))
#         last_pos = list(i.pos())
#     else:
#         last_pos = list(i.pos())
#         i.goto(x=-249, y=(last_pos[1] - 33))

all_turtles = []

is_race_on = False
if user_bet:
    is_race_on = True

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[(i - 1) + 1])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=(-100 + i * 33))
    all_turtles.append(new_turtle)


while is_race_on:
    for turtle in all_turtles:
        turtle.speed("fastest")
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The winning color is {winning_color}")
            else:
                print(f"You've lost! The winning color is {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
