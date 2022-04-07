
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.r_score = 0
        self.l_score = 0

        self.update()

    def update(self):
        self.clear()
        self.goto(x =100, y=200)
        self.write(self.r_score, align= "Center", font=("Courier", 80, "normal"))
        self.goto(x=-100, y=200)
        self.write(self.l_score, align= "Center", font=("Courier", 80, "normal"))


    def right_score(self):
        self.r_score += 1
        self.update()


    def left_score(self):
        self.l_score += 1
        self.update()





