from turtle import Turtle

STARTING_GRID = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):


        self.segment = []
        self.create_snake()


    def create_snake(self):
        for grid in STARTING_GRID:
            self.add_segment(grid)


    def add_segment(self,grid):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(grid)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)

        self.segment[0].forward(MOVE_FORWARD)

    def Up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def Down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def Left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def Right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
