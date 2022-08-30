import time
from turtle import Turtle, Screen

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Drawing the body of snake
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)


def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_right():
    turtle.setheading(turtle.heading() + 10)


def turn_left():
    turtle.setheading(turtle.heading() - 10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def init_game():
    turtle.pensize()


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(1)
    for segment in segments:
        if segment.xcor() > 260:
            is_game_on = False
        else:
            segment.forward(20)


# screen.listen()
# screen.onkey(move_forward(), "w")
# screen.onkey(move_backwards(), "s")
# screen.onkey(turn_left(), "a")
# screen.onkey(turn_right(), "d")
# screen.onkey(clear, "c")
screen.exitonclick()
