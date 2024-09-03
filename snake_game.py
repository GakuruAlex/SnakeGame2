from turtle import Turtle
STARTING_COORD = [(0,0), (20, 0), (40, 0)]
FORWARD = 20
class Snake:
    def __init__(self):
        self.snakes = []
        self.snake()
        self.head = self.snakes[0]


    def snake(self):
        for coord in STARTING_COORD:
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.speed(1)
            turtle.penup()
            turtle.goto(coord)
            self.snakes.append(turtle)
    def move_snake(self):
        snake_len = len(self.snakes)
        for i in range(0,snake_len-1, 1):
            x_y_cor =  self.snakes[i].pos()
            self.snakes[i+1].goto(x_y_cor)
        self.head.forward(FORWARD)
