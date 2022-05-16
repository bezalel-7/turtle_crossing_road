from turtle import Turtle

class level(Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 0
        self.penup()
        self.newlevel()
    def newlevel(self):
        self.color("white")
        self.hideturtle()
        self.clear()
        self.goto(x=-260,y=260)
        self.write(arg=f"LEVEL={self.Level}" , align="left", font=("bold" , 20 ,"bold"))
        self.Level += 1

