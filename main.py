from turtle import Screen
from time import sleep
from snake_game import Snake
from food import Food
from scoreboard import ScoreBoard
def main() -> None:
    screen = Screen()
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
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
        if food.distance(snake.head) < 20:
            food.make_food()
            scoreboard.increase_score()
            snake.add_tail()
        if snake.detect_collision_with_tail():
            game_is_on = False
            scoreboard.end_game()
        if snake.has_collided_with_walls():
            game_is_on = False
            scoreboard.end_game()


    screen.exitonclick()


if __name__ == "__main__":
    main()