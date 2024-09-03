from turtle import Screen
from time import sleep
from snake_game import Snake
def main() -> None:
    screen = Screen()
    screen.tracer(0)
    snake = Snake()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    game_is_on = True

    while game_is_on:
        sleep(1)
        screen.update()
        screen.tracer(1)
        snake.move_snake()
        screen.listen()
        screen.tracer(0)
        screen.onkey(snake.move_up, "Up")
        screen.onkey(snake.move_down,"Down")
        screen.onkey(snake.move_left,"Left")
        screen.onkey(snake.move_right, "Right")
    
    
    
    
    screen.exitonclick()


if __name__ == "__main__":
    main()