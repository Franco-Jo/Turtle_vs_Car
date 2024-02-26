
#  TODO make cars not overllap
import time
from car import Car
import random

STARTING_POSITIONS = [(-1000, -400), (1000, -200), (-1000, 0), (1000, 200), (-1000, 400)]


COLORS = ['red', 'yellow', 'purple', 'orange', 'brown', 'pink']


class CarManager:

    def __init__(self):
        self.cars = []
        self.add_car()

    def generate_cars(self):

        self.add_car()

        self.make_traffic()

    def add_car(self):
        is_merging = True

        while is_merging:
            should_remove = False
            new_car = Car(random.choice(COLORS), (random.choice(STARTING_POSITIONS)))

            for car in self.cars:

                if new_car.distance(car) < 100:
                    should_remove = True

            self.make_traffic()

            if should_remove:

                self.make_traffic()
                del new_car
            elif new_car.ycor() == -200 or new_car.ycor() == 200:
                new_car.west_bound()

                self.cars.append(new_car)
                is_merging = False

            else:
                self.make_traffic()
                self.make_traffic()
                self.cars.append(new_car)
                is_merging = False

    def make_traffic(self):
        for car in self.cars:
            car.move_car(random.randint(1,8))
