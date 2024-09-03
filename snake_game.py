from turtle import Turtle
STARTING_COORD = [(-20,0), (0, 0), (20, 0)]
FORWARD = 20
UP = 90
RIGHT = 0
LEFT= 180
DOWN = 270
class Snake:
    def __init__(self):
        self.snakes = []
        self.make_snake()
        self.head = self.snakes[0]


    def snake(self, position):
            turtle = Turtle()
            turtle.setheading(180)
            #turtle.shapesize(stretch_len=2, stretch_wid= 4)
            turtle.shape("square")
            turtle.color("white")
            turtle.speed(1)
            turtle.penup()
            turtle.goto(position)
            self.snakes.append(turtle)
    def make_snake(self):
        for coord in STARTING_COORD:
            self.snake(coord)

    def move_snake(self):
        snake_len = len(self.snakes)
        for i in range(snake_len-1,0, -1):
            x_y_cor =  self.snakes[i-1].pos()
            self.snakes[i].goto(x_y_cor)
        self.head.forward(FORWARD)
    def move_up(self):
            self.head.setheading(UP)
    def move_down(self):
        self.head.setheading(DOWN)
    def move_left(self):
        self.head.setheading(LEFT)
    def move_right(self):
        self.head.setheading(RIGHT)