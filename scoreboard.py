from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(300, 265)
        self.write("Score: " + str(self.score), align="center", font=("Courier", 15, "normal"))

    def brick_destroyed(self):
        self.score += 1
        self.print_score()

