import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")



game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    screen.update()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level_up()
        car_manager.car_speed_up()

    for cars in car_manager.all_cars:
        if player.distance(cars) < 10:
            game_is_on = False
            scoreboard.end_game()










screen.exitonclick()
