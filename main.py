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

    # The moving way of a snake: the 3rd segment moves to the 2nd segment's spot,
    # then the 2nd segment moves to the 1st segment's position.
    # The first segment will go the direction user assigned from user input
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    segments[0].forward(20)

    if segments[0].xcor() > 280 or segments[0].ycor() > 280:
        is_game_on = False


# screen.listen()
# screen.onkey(move_forward(), "w")
# screen.onkey(move_backwards(), "s")
# screen.onkey(turn_left(), "a")
# screen.onkey(turn_right(), "d")
# screen.onkey(clear, "c")
screen.exitonclick()
