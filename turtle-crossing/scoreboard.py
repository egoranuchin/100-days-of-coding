from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.level_no = 1
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(position)
        self.update_scoreboard()

    def level_increase(self):
        self.level_no += 1
        self.clear()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.level_no}", False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, font=FONT)
