
from turtle import Turtle
# CREATE CONSTANTS

#1- CREATE SIZE
PADDLE_WITH = 5
PADDLE_len = 1



class Paddle(Turtle):

    def __init__(self, pos = (0, 0)):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WITH, stretch_len=PADDLE_len)
        self.penup()
        self.goto(pos)


    def move_up(self):
        x_up = self.xcor()
        y_up = self.ycor()
        self.goto(x=x_up, y=y_up + 20)

    def move_down(self):
        x_down = self.xcor()
        y_down = self.ycor()
        self.goto(x = x_down, y= y_down-20)













