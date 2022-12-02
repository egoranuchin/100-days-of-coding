from turtle import Turtle
# from food import Food

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
# score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 270)
        self.update_scoreboard()
    #
    def score_increase(self):
        # global score
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)