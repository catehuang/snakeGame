import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

INIT_SPEED = 0.5
REDUCE_RATE = 1.5

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.delay(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
rate = INIT_SPEED

while is_game_on:
    screen.update()
    time.sleep(rate)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        rate /= REDUCE_RATE

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        play_again = screen.textinput(title="Play again?", prompt="Do you want to play again? (y/n): ")
        if play_again == "y":
            screen.listen()
            scoreboard.reset()
            snake.reset()
            rate = INIT_SPEED
        else:
            is_game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            play_again = screen.textinput(title="Play again?", prompt="Do you want to play again? (y/n): ")
            if play_again == "y":
                screen.listen()
                scoreboard.reset()
                snake.reset()
                rate = INIT_SPEED
            else:
                is_game_on = False

screen.exitonclick()
