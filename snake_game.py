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
            turtle.shape("square")
            turtle.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
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
    def add_tail(self):
        x_cor = self.snakes[-1].xcor()
        y_cor = self.snakes[-1].ycor()
        self.snake((x_cor, y_cor))
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading()  != UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def detect_collision_with_tail(self):
        for snake in self.snakes[1:]:
            if self.head.distance(snake) < 10:
                return True
    def has_collided_with_walls(self):
        return self.head.xcor() > 390 or self.head.xcor() < -390 or self.head.ycor() > 290 or self.head.ycor() < -290
