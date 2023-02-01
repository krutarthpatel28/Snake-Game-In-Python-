import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
score = ScoreBoard()
snake = Snake()

screen.listen()
screen.onkey(snake.Up, 'Up')
screen.onkey(snake.Down, 'Down')
screen.onkey(snake.Left, 'Left')
screen.onkey(snake.Right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #     detecting collision from food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or \
            snake.segment[0].ycor() < -280:
        score.coli_with_wall()
        score.restart_game_promt()
        game_is_on = False

    for segment in snake.segment:
        if segment == snake.segment[0]:
            pass
        elif snake.segment[0].distance(segment) < 10:
            score.coli_with_wall()
            score.restart_game_promt()
            game_is_on = False

screen.exitonclick()
