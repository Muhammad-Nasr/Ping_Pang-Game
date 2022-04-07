
from turtle import Turtle, Screen


class Ball (Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_speed = .1
        self.x = 10
        self.y = 10

    def move(self):

        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.ball_speed *= .9
        
    def reset_game(self):
        self.ball_speed = .1
        self.goto(0, 0)
        self.bounce_x()













