from turtle import Turtle


class Car(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.wheels = []
        self.make_body(color, position)
        self.make_wheels()

    def make_body(self, color, position):
        self.shape('square')
        self.fillcolor(color)
        self.pensize(2)
        self.shapesize(stretch_wid=2.5, stretch_len=4, outline=2)
        self.pu()
        self.goto(position)

    def make_wheels(self):
        for _ in range(4):
            new_wheel = Turtle('square')
            new_wheel.pu()
            new_wheel.shapesize(stretch_len=.90, stretch_wid=.16)
            self.wheels.append(new_wheel)

        self.wheels[0].goto(self.xcor() + 22, self.ycor() + 28)
        self.wheels[1].goto(self.xcor() + 22, self.ycor() - 28)
        self.wheels[2].goto(self.xcor() - 18, self.ycor() + 28)
        self.wheels[3].goto(self.xcor() - 18, self.ycor() - 28)

    def move_car(self, speed):

        self.forward(speed)
        for wheel in self.wheels:
            wheel.forward(speed)

    def west_bound(self):
        self.setheading(180)
        for wheel in self.wheels:
            wheel.setheading(180)

    def east_bound(self):
        self.setheading(0)
        for wheel in self.wheels:
            wheel.setheading(0)
