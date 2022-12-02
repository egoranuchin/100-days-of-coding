import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)

# tim.right(90)
# tim.forward(20)
# tim.right(90)
# tim.forward(20)
# tim.right(90)
# tim.forward(20)
# tim.right(90)
# tim.forward(20)

# for i in range(15):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# # TODO: random walk, turns = 90 degrees, fast, each movement with different colour, thickness the size of the turtle shape
#
# directions = [0, 1, 2, 3]
#
#
# def east():
#     tim.forward(20)
#
#
# def south():
#     tim.right(90)
#     tim.forward(20)
#     tim.left(90)
#
#
# def west():
#     tim.right(90)
#     tim.right(90)
#     tim.forward(20)
#     tim.left(90)
#     tim.left(90)
#
#
# def north():
#     tim.right(90)
#     tim.right(90)
#     tim.right(90)
#     tim.forward(20)
#     tim.left(90)
#     tim.left(90)
#     tim.left(90)


# def random_walk(direction):
#     tim.width(10)
#     # tim.color(random.choice(colours))
#     tim.color(random_color())
#     tim.speed(10)
#     # draw_shape(shape_side_n)
#     if direction == 0:
#         east()
#     elif direction == 1:
#         south()
#     elif direction == 2:
#         west()
#     elif direction == 3:
#         north()


def draw_circle():
    tim.circle(100)
    tim.color(random_color())
    tim.speed("fastest")


def solution(size_of_gap):
    # Spirograph:
    for _ in range(int(360/size_of_gap)):
        draw_circle()
        tim.setheading(tim.heading() + size_of_gap)
    # Naive spirograph:
    # for i in range(36):
    #     tim.right(10)
    #     draw_circle()
    # Random walk:
    # for walk in range(100):
    #     direction = random.choice(directions)
    #     random_walk(direction)


solution(5)

screen = t.Screen()
screen.exitonclick()

