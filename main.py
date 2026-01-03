import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Capstone Project")
screen.tracer(0)


car_manager=CarManager()
game_is_on = True

player=Player()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player.front)
screen.onkey(key="Down",fun=player.backward)


timer=0.125

while game_is_on:
    time.sleep(timer)
    screen.update()
    car_manager.move()
    car_manager.refresh()
    for i in car_manager.segments:
        if player.distance(i)<12:
            scoreboard.gameover()
            game_is_on=False

    if player.ycor()>280.00:
        scoreboard.add_score()
        player.goto(0.00, -280)
        timer-=0.005

screen.exitonclick()