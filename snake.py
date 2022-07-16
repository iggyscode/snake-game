import turtle
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
      self.segments_arr = []
      self.create_snake()
      self.head = self.segments_arr[0]

    def move(self):
        for segment_num in range(len(self.segments_arr) - 1, 0, -1):
            new_x = self.segments_arr[segment_num -1].xcor()
            new_y = self.segments_arr[segment_num - 1].ycor()
            self.segments_arr[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            self.segment = turtle.Turtle("square")
            self.segment.color("white")
            self.segment.penup()
            self.segment.goto(x=x_cor, y=0)
            self.segments_arr.append(self.segment)
            x_cor -= 20

    def snake_extend(self):
        self.segment = turtle.Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.goto(self.segments_arr[-1].position())
        self.segments_arr.append(self.segment)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

        


        
