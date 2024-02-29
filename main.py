# Breakout game, by rogertxe, February 2024
# Create the screen

from turtle import Screen, Turtle
from brick import Brick
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from lives import Livestracker
import message
import time
import random

game_ongoing = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BREAKOUT GAME")
screen.tracer(0)

# Define the colors for the bricks
brick_colors = ["red", "blue", "green", "yellow", "white", "brown"]

# Define the starting position for the bricks
start_x = -340
start_y = 240

def create_bricks():
    bricks = []
    total_bricks = 0
    # Create bricks in multiple rows
    for row in range(6):  # Create 6 rows of bricks
        for column in range(13):  # Create 13 bricks per row
            # Calculate the position of each brick
            x = start_x + column * 56
            y = start_y - row * 32
            # Choose a random color for the brick
            color = random.choice(brick_colors)
            # Create the brick
            brick = Brick(position=(x, y), color=color)
            bricks.append(brick)  # Add the brick to the list
            total_bricks += 1
    return bricks, total_bricks

# Create the bricks at the start of the game
bricks, total_bricks = create_bricks()

# Create the paddle
paddle = Paddle((0, -300), "blue")

# Create the ball
ball = Ball()

# Create the scoreboard
scoreboard = Scoreboard()

# Create lives tracker
lives = Livestracker()

# Move paddle
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

# Define game_ongoing outside the function
game_ongoing = True

def play_again():
    global bricks, total_bricks, game_ongoing
    
    play_again = screen.textinput("Game Over", "Do you want to play again? (y/n): ").lower()
        
    if play_again == 'y':

        # Clear existing bricks from the screen
        for brick in bricks:
            brick.destroy_brick()  # Remove the brick from the screen

        # Recreate bricks
        bricks, total_bricks = create_bricks()

        # Reset the paddle position
        paddle.goto(0, -300)

        # Reset the ball position and direction
        ball.reset_position()

        # Reset the scoreboard
        scoreboard.score = 0
        scoreboard.print_score()

        # Reset the lives tracker
        lives.lives = 3
        lives.print_score()

        # Move paddle
        screen.listen()
        screen.onkeypress(paddle.move_left, "Left")
        screen.onkeypress(paddle.move_right, "Right")

        # Restart the game
        game_ongoing = True

    else:
        game_ongoing = False
        screen.clear()


while game_ongoing:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    
    # detect collision with lateral walls and bounce
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        ball.bounce_x()
    
    # detect collision with superior wall and bounce
    if ball.ycor() >= 290:
        ball.bounce_y()
    
    # detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -270:
        ball.bounce_y()
    
    # brick collision
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.destroy_brick()
            ball.bounce_y()
            scoreboard.brick_destroyed()
            total_bricks -= 1

    # player misses
    if ball.ycor() <= -320:
        ball.reset_position()
        lives.life_lost()

    # player wins
    if total_bricks == 0:
        bricks[-1].destroy_brick()
        screen.update()
        global win_writer
        global game_over_writer
        win_writer = message.display_win()
        play_again()
        message.erase_win(win_writer)

    # game over
    if lives.lives == 0:
        game_over_writer = message.display_game_over()
        play_again()
        message.erase_game_over(game_over_writer)

screen.exitonclick()
