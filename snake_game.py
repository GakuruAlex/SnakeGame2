from turtle import Turtle
STARTING_COORD = [(0,0), (20, 0), (40, 0)]
class Snake:
    def __init__(self):
        self.snakes = []
        self.head = STARTING_COORD[0]
        self.snake()

    def snake(self):
        for coord in STARTING_COORD:
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(coord)
            self.snakes.append(turtle)
        
