from turtle import Screen
from player import Player
from car_manager import CarManager

import time
from car import Car

game_window = Screen()
game_window.setup(width=1900, height=1200)
game_window.tracer(0)

player = Player()
car_manager = CarManager()
#car = Car('red', (0, 0))


game_window.listen()
game_window.onkey(fun=player.move_up, key='Up')
game_window.onkey(fun=player.move_left, key='Left')
game_window.onkey(fun=player.move_right, key='Right')


game_is_on = True

while game_is_on:

    game_window.update()
    time.sleep(0.1)

    car_manager.generate_cars()





game_window.exitonclick()