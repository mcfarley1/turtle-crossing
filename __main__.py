import time
from turtle import Screen
from .player import Player, FINISH_LINE_Y
from .car_manager import CarManager
from .scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_move()
    car_manager.remove_car()

    # If car hits player.
    for car in car_manager.car_list:
        if car.xcor() - 28 <= player.xcor() <= car.xcor() + 28 and car.ycor() - 22 <= player.ycor() <= car.ycor() + 22:
            scoreboard.game_over()
            if scoreboard.level > scoreboard.high_score:
                initials = screen.textinput("Turtle Crossing", "Enter your initials: ")
                screen.listen()
                scoreboard.high_score_name = initials.upper()
                scoreboard.update_high_score()
            game_is_on = False

    # If player crosses finish line.
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.score()
        player.reposition()
        car_manager.speed_up()

screen.exitonclick()
