from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Scoreboard = {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.clear()
        self.goto(0, 270)
        self.score += 1
        self.write(f"Score = {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)
