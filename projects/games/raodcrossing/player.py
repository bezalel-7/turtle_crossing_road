from turtle import Turtle
from scoreboard import level
l  = level()
l.hideturtle()
ISTEPS = 5
INCREMENTSTEPS = 10
class Player(Turtle):
         def __init__(self):
             super().__init__()
             self.shape("turtle")
             self.penup()
             self.color("white")
             self.reset()
             self.setheading(90)
             self.move()

         def move(self):
             if(self.ycor() > 280):
                 self.reset()
             else:
              new_y = self.ycor() + l.Level + ISTEPS
              self.goto(x=0, y = new_y)
         def reset(self):
             self.goto(x=0, y=-280)
             l.newlevel()
