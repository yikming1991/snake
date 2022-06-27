import turtle as t
import random

class Food(t.Turtle):  # inherits the Turtle() class, not turtle module

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=.8, stretch_wid=.8)
        self.speed("fastest")
        xcor = random.choice(range(-260, 260, 20))
        ycor = random.choice(range(-260, 260, 20))
        self.goto(xcor, ycor)
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))