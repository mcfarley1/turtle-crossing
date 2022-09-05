import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_DENSITY = 20


class CarManager:

    def __init__(self):
        self.car_list = []
        self.generate_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        for num in range(CAR_DENSITY):
            tim = Turtle()
            tim.color(random.choice(COLORS))
            tim.penup()
            tim.shape("square")
            tim.shapesize(stretch_wid=1, stretch_len=2)
            tim.setheading(180)
            tim.goto(random.randint(330, 930), random.randint(-250, 250))
            self.car_list.append(tim)

    def car_move(self):
        for car in self.car_list:
            car.forward(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT

    def remove_car(self):
        for car in self.car_list:
            if car.xcor() < -330:
                car.goto(random.randint(330, 930), random.randint(-250, 250))
