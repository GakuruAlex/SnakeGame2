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
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)
