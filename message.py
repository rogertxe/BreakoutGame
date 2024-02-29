from turtle import Turtle

# Create a function to display "Game Over" message
def display_game_over():
    game_over_writer = Turtle()
    game_over_writer.color("red")
    game_over_writer.penup()
    game_over_writer.hideturtle()
    game_over_writer.goto(0, 260)
    game_over_writer.write("Game Over", align="center", font=("Courier", 20, "bold"))
    return game_over_writer  # Return the Turtle object

# Function to erase "Game Over" message from screen
def erase_game_over(game_over_writer):
    game_over_writer.clear()

def display_win():
    win_writer = Turtle()
    win_writer.color("green")
    win_writer.penup()
    win_writer.hideturtle()
    win_writer.goto(0, 260)
    win_writer.write("You win!", align="center", font=("Courier", 20, "bold"))
    return win_writer  # Return the Turtle object

# Function to erase "Game Over" message from screen
def erase_win(win_writer):
    win_writer.clear()