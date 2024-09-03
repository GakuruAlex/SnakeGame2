from turtle import Screen
from snake_game import Snake
def main() -> None:
    screen = Screen()
    snake = Snake()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    
    
    
    
    screen.exitonclick()


if __name__ == "__main__":
    main()