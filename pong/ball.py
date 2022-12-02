from turtle import Turtle

#TODO 3: Make a white ball class width 20, h 20, x_pos,y_pos = 20, x and y change with each screen update change x and y pos to another value, leading to the upper right corner of the screen

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        # self.speed("fastest")
        self.pu()
        self.goto(0, 0)
        self.ball_speed = 10
        self.x_move = self.ball_speed
        self.y_move = self.ball_speed


    def move(self):
        new_x = (self.xcor() + self.x_move)
        new_y = (self.ycor() + self.y_move)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)

    def increase_speed(self):
        self.ball_speed *= 100

