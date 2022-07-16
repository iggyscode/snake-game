from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.random_location()

    def random_location(self):
        random_coor = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(random_coor)

        
