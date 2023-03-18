import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
TIME_SLEEP = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Create turtle and move
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(TIME_SLEEP)
    screen.update()
    # create cars and move them
    car_manager.create_car()
    car_manager.move_cars()
    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
    # Detect collision with wall
    if player.ycor() == 280:
        player.goto((0, -280))
        TIME_SLEEP *= 0.8
        scoreboard.increase_level()
        scoreboard.update_level()


screen.exitonclick()
