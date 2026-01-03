COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# position=[(300,-280),(300,-240),(300,-200),(300,-160),(300,-120),(300,-80),(300,-40),(300,0)]
from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.segments=[]
        for i in range(30):
            self.add_segment()

    def add_segment(self):
        paddle=Turtle()
        paddle.penup()
        paddle.shape("square")
        paddle.speed("fastest")
        paddle.setheading(180)
        paddle.goto(x=random.randrange(-280,300,40),y=random.randrange(start=-240,stop=280,step=50))
        paddle.shapesize(stretch_wid=1,stretch_len=2)
        paddle.color(random.choice(COLORS))
        self.segments.append(paddle)

    def move(self):
        for i in self.segments:
            i.forward(20)

    def refresh(self):
        for i in self.segments:
            if i.xcor() < -320:
                i.goto(x=random.randrange(300, 400, 80), y=random.randrange(start=-300, stop=300, step=80))









