# Create and operate the paddle

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, initial_position, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=4, outline=None)
        self.color(color)
        self.goto(initial_position)
        self.speed("fastest")

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

