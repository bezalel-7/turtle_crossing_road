from turtle import Screen
from player import Player
import time
from obstructions import Obstruction
from scoreboard import level

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
obs = Obstruction()
# Level = level()
screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    obs.createobs()
    obs.move()
    for car in obs.cars:
        if player.distance(car) < 33:
            player.write(arg="GAME OVER!!!", align="center", font=("white", 50, "bold"))
            game_is_on = False
screen.exitonclick()
