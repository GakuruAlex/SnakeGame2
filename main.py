from turtle import Screen
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
        screen.tracer(1)
        snake.move_snake()
    
    
    
    
    screen.exitonclick()


if __name__ == "__main__":
    main()