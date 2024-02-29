from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(1.4, 2.6)
        self.penup()
        self.goto(position)

    def destroy_brick(self):
        self.goto(1000, 1000)  # Move the brick to an off-screen location
        self.hideturtle()  # Hide the brick