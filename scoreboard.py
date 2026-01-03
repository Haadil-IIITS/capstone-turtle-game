FONT = ("Courier", 24, "normal")

from turtle import Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(240,260)
        self.score=0
        self.write(f"{self.score}",False,"center",font=FONT)

    def add_score(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}", False, "center", font=("Courier", 30 , "normal"))


    def gameover(self):
        self.goto(0.00,0.00)
        self.write("Game Over",False,"center",font=FONT)