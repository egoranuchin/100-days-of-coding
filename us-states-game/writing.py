from turtle import Turtle

class Writing(Turtle):

    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.write(state)
        self.goto(x, y)