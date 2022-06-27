import turtle as t
import snake
import time
import food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
t.tracer(0)

board = Scoreboard()
food = food.Food()
boa = snake.Snake()
screen.listen()
screen.onkeypress(fun=boa.turn_north, key="w")
screen.onkeypress(fun=boa.turn_south, key="s")
screen.onkeypress(fun=boa.turn_west, key="a")
screen.onkeypress(fun=boa.turn_east, key="d")

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.05)      # delays the screen refresh by integer set in sleep()
    boa.move()

    # Detects collision of snake head with food
    if boa.head.distance(food) < 15:
        food.refresh()
        boa.extend()
        board.increase_score()

    # Detects collision of snake head with wall
    if boa.head.xcor() > 280 or boa.head.xcor() < -280 or boa.head.ycor() > 280 or boa.head.ycor() < -280:
        board.reset()
        boa.reset()

    # Detects collision of snake head with tail
    for segment in boa.snake[1:]:
        if boa.head.distance(segment) < 15:
            board.reset()
            boa.reset()

screen.exitonclick()