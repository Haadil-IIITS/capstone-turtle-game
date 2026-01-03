STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0.00,-280)
        self.color("white")
        self.shape("turtle")

    def front(self):
        self.setheading(90)
        self.forward(20)

    def backward(self):
        self.setheading(270)
        self.forward(20)



