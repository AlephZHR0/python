from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5
        self.move_increment = 10

    def new_car(self):
        random_chance = randint(1, 5)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.setheading(180)
            car.shapesize(1, 2)
            car.color(choice(COLORS))
            car.goto(300, randint(-250, 250))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.starting_move_distance)

    def increase_car_speed(self):
        self.starting_move_distance += self.move_increment
