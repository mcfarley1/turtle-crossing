import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
SPEED_VARIATION = 2
CAR_DENSITY = 20


class CarManager:

    def __init__(self):
        self.car_list = []
        self.speed_list = []
        self.generate_car()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.generate_speed()

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

    def generate_speed(self):
        for num in range(CAR_DENSITY):
            self.speed_list.append(random.randint(self.move_distance - SPEED_VARIATION,
                                                  self.move_distance + SPEED_VARIATION))

    def car_move(self):
        for num in range(len(self.car_list)):
            self.car_list[num].forward(self.speed_list[num])

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
        self.speed_list = []
        self.generate_speed()

    def remove_car(self):
        for car in self.car_list:
            if car.xcor() < -330:
                car.goto(random.randint(330, 930), random.randint(-250, 250))
