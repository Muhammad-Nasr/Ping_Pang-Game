# create the screen

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()

screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.title("pang")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

# def keys for movement

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    elif ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() <-325:
        ball.bounce_x()

    elif ball.xcor() > 380 :
        ball.reset_game()
        score_board.left_score()

    elif ball.xcor() < -380:
        ball.reset_game()
        score_board.right_score()












screen.exitonclick()











