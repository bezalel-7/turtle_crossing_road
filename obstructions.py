from turtle import Turtle
from player import l
# import random
COLORS =["red","blue","green","orange","white","yellow"]
X = 5
IX = 10
import random
class Obstruction(Turtle):
          def __init__(self):
              super().__init__()
              self.cars = []
              self.hideturtle()
              self.createobs()
          def createobs(self):
            if random.randint(1,6) == 1:
              newcar = Turtle("square")
              newcar.shapesize(stretch_wid=1, stretch_len=2.5)
              newcar.color(random.choice(COLORS))
              newcar.penup()
              obb =  random.randint(-250,250)
              newcar.goto(x=280,y=obb)
              self.cars.append(newcar)
          def move(self):
                for car in self.cars:
                  car.backward(X+l.Level)
