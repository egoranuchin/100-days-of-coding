from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
# score = 0

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(position)
        self.update_scoreboard()
    #
    def score_increase(self):
        # global score
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)