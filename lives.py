from turtle import Turtle


class Livestracker(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-310, 265)
        self.write("Lives: " + str(self.lives), align="center", font=("Courier", 15, "normal"))

    def life_lost(self):
        self.lives -= 1
        self.print_score()

