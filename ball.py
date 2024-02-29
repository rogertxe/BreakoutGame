# Create and control the ball
import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7, 0.7)
        self.penup()
        self.set_direction()
        self.move_speed = 0.04

    def reset_position(self):
        self.goto(0, 0)
        self.set_direction()

    def set_direction(self):
        angle = random.uniform(190, 350)  # Random angle between 190 and 350 degrees
        self.setheading(angle)

    def move_ball(self):
        self.forward(10)  # Move the ball forward with a constant speed

    def bounce_y(self):
        current_heading = self.heading()
        self.setheading(360 - current_heading)  # Reflect the angle in y-axis
    
    def bounce_x(self):
        current_heading = self.heading()
        self.setheading(180 -current_heading)  # Reflect the angle in x-axis
