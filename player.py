from turtle import Turtle

MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.fillcolor('green')
        self.pensize(2)
        self.shapesize(stretch_wid=2.5, stretch_len=2.5, outline=2)
        self.pu()
        self.setheading(90)
        self.goto(0, -550)

    def move_up(self):
        """turn player to the north and move forward"""
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        """turn player to the west and move forward"""
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        """turn player to the east and move forward"""
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
