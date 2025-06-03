from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """Represents and manages the snake's body — a sequence of segments """
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """Create snake body and starting position"""
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Method controls how to snake move forward"""
        # start= 2, stop= 0, step= -1
        for seg_num in range(len(self.segments) - 1, 0, -1): 
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)