from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


def get_high_score():
    with open("data.txt", mode="r") as file:
        high_score = int(file.read())
        return high_score


def set_high_score(new_high_score):
    with open("data.txt", mode="w") as file:
        file.write(f"{new_high_score}")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):

        if self.score > self.high_score:
            # self.high_score = self.score
            set_high_score(str(self.score))
            self.high_score = get_high_score()
        self.score = 0
        self.update_scoreboard()
