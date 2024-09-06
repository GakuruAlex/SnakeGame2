from turtle import Turtle
FONT = ('Arial', 18, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.display_score()

    def write_high_score(self, score):
        with open("high_score.txt", mode="w") as file:
            file.write(f"HighScore, {score}")
    def read_high_score(self):
        try:
            with open("high_score.txt", mode="r") as file:
                high_score = file.read().split(",")[1]
            return int(high_score)
        except FileNotFoundError:
            return 0
    def display_score(self):
        self.high_score = self.read_high_score()
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", font=FONT)
    def increase_score(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.read_high_score():
            self.write_high_score(self.score)
        self.score = 0
        self.display_score()
   