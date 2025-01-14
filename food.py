from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        loc_x = random.randint(-280, 280)
        loc_y = random.randint(-280, 280)
        self.goto(loc_x, loc_y)

    def refresh(self):
        loc_x = random.randint(-280, 280)
        loc_y = random.randint(-280, 280)
        self.goto(loc_x, loc_y)
