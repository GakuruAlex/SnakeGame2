from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.penup()
        self.make_food()
    def make_food(self):
        x_cor = randint(-380, 380)
        y_cor = randint(-280, 280)
        self.goto(x= x_cor, y= y_cor)
