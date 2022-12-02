# TODO 2: Create a paddle with parameters: width 20, height 100, x_pos 350, y_pos 0. Up and down arrows to move for 20 pxl

from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (-350, 0)]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.goto(position)

    #
    # def add_paddle(self, position):
    #     paddle = Turtle()
    #     paddle.shape("square")
    #     paddle.shapesize(stretch_wid=5, stretch_len=1)
    #     paddle.color("white")
    #     paddle.speed("fastest")
    #     paddle.pu()
    #     paddle.goto(position)

    # def create_paddle(self, position):
    #     # for position in STARTING_POSITIONS:
    #     self.add_paddle(position)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        # screen.update()
        # paddle.setheading(270)
        # paddle.forward(20)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        # screen.update()
        # paddle.setheading(90)
        # paddle.forward(20)
