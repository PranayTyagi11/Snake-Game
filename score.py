from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(250)
        self.write(f"Score: {self.score}", align='center', font=("Arial", 24, "normal"))

    def score_incrementer(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.hideturtle()
        self.color("red")
        self.sety(0)
        self.write("GAME OVER", font=("Arial", 30, "normal"), align="center")

