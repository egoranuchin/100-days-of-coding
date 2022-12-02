# import colorgram as c
import random
import turtle as t

t.colormode(255)
tim = t.Turtle()

# rgb_colors = []
# colors = c.extract('1e7fdd7d36fd4ff5e627851d801da345.jpg', 9)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(29, 106, 143), (231, 152, 76), (7, 56, 96), (16, 168, 205), (145, 77, 30)]

# TODO: make a painting 10 on 10 dots, the size of a dot is 20, the distance between dots is 50, the color of each dot is random

def random_color():
    color = random.choice(color_list)
    return color


def draw_dot():
    color = random_color()
    tim.dot(20, color)

def draw_row():
    for _ in range(10):
        draw_dot()
        tim.forward(50)

def painting():
    tim.pu()
    tim.hideturtle()
    tim.speed("fastest")
    for _ in range(10):
        draw_row()
        tim.left(180)
        tim.forward(500)
        tim.right(90)
        tim.forward(50)
        tim.right(90)


painting()

screen = t.Screen()
screen.screensize(1024, 1024)
screen.exitonclick()
