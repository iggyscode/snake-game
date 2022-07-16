from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

game = True
snake = Snake()
food = Food()
score = Score()


screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Check if the snake hit any side of the wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        score.game_over()
        game = False

    #Check if the snake touched the food
    if snake.head.distance(food) < 15:
        food.random_location()
        score.increase_score()      
        snake.snake_extend()
    
    #Check if the snake hit itself
    for segment in snake.segments_arr[2:]:
      if snake.head.distance(segment) < 15:
            game = False
            score.game_over()
            break




screen.exitonclick()