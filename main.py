from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("#06038D")
screen.title("Snake Game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    snake.move()

    # Detect collision with food.
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        score.score_incrementer()
        snake.extend()

    x_boundary_window = -280 > snake.turtles[0].xcor() or 280 < snake.turtles[0].xcor()
    y_boundary_window = -280 > snake.turtles[0].ycor() or 280 < snake.turtles[0].ycor()

    if x_boundary_window or y_boundary_window:
        score.game_over()
        game_is_on = False

    for t in snake.turtles[1:]:
        if t.distance(snake.turtles[0]) < 10:
            score.game_over()
            game_is_on = False
    
screen.exitonclick()
