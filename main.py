from turtle import Screen
from time import sleep
from snake_game import Snake
from food import Food
def main() -> None:
    screen = Screen()
    screen.tracer(0)
    snake = Snake()
    food = Food()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    game_is_on = True

    while game_is_on:
        sleep(0.2)
        screen.update()
        snake.move_snake()
        screen.listen()
        screen.onkey(snake.move_up, "Up")
        screen.onkey(snake.move_down,"Down")
        screen.onkey(snake.move_left,"Left")
        screen.onkey(snake.move_right, "Right")
        if food.distance(snake.head) < 10:
            food.make_food()

    screen.exitonclick()


if __name__ == "__main__":
    main()