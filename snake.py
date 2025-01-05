from turtle import Turtle


class Snake:

    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.turtles = []

        for position in self.positions:
            self.add_turtle(position)

    def add_turtle(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("gold")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())
    def up(self):
        self.turtles[0].setheading(90)

    def down(self):
        self.turtles[0].setheading(270)

    def left(self):
        self.turtles[0].setheading(180)

    def right(self):
        self.turtles[0].setheading(0)

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[num - 1].xcor()
            y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(x, y)

        self.turtles[0].forward(20)
