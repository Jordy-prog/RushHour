import random
from time import sleep

from ..classes import car


def random_pure(RushHour):
    '''
    Implementation of the random algorithm.
    Picks a random car until it finds a car that can move, then moves it.
    '''
    while True:
        car = random.choice(list(RushHour.cars.values()))
        free_space = car.look_around(RushHour)
        
        if free_space['rear'] or free_space['front']:
            break

    distance = random.randrange(free_space['rear'], free_space['front'] + 1)
    RushHour.move(car, distance)

def random_constraint(RushHour):
    '''
    Implements the random algorithm.

    Adds an extra constraint to the 'random_pure' function:
    Makes sure a car can't undo its last move, 
    this is done to prevent the algorithm from just moving a car back and forth.
    '''
    chosen_cars = []

    # picks a random car until it finds one that can move
    while True:
        # a loop to make sure the algorithm doesn't pick the same car multiple times if it can't move
        while True:
            car = random.choice(list(RushHour.cars.values()))

            if not car in chosen_cars:
                chosen_cars.append(car)
                break

        free_space = car.look_around(RushHour)
        distance = 0

        # if a car can move, determine a random distance to move the car
        if free_space['rear'] or free_space['front']:
            while distance == 0:
                distance = random.randrange(free_space['rear'], free_space['front'] + 1)
                
        # continues if move is the exact opposite of last move, else breaks
        if not (car, - distance) == RushHour.last_move and distance:
            break

    RushHour.move(car, distance)