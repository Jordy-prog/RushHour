import random
from ..classes import car
from time import sleep

def random_pure(RushHour):
    while True:
        car = random.choice(list(RushHour.cars.values()))
        free_space = car.look_around(RushHour)
        
        if free_space['rear'] or free_space['front']:
            break

    distance = random.randrange(free_space['rear'], free_space['front'] + 1)
    RushHour.move(car, distance)

def random_constraint(RushHour):
    chosen_cars = []

    while True:
        while True:
            car = random.choice(list(RushHour.cars.values()))

            if not car in chosen_cars:
                chosen_cars.append(car)
                break

        free_space = car.look_around(RushHour)
        distance = 0

        if free_space['rear'] or free_space['front']:
            while distance == 0:
                distance = random.randrange(free_space['rear'], free_space['front'] + 1)
                
        if not (car, - distance) == RushHour.last_move and distance:
            break

    RushHour.move(car, distance)