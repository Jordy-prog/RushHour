import os
import random
from time import sleep

from ..classes import car

def manager(RushHour, algorithm):
    # asks user if he wants results to be printed
    to_print = None

    while to_print not in ['yes', 'y', 'no', 'n']:
        to_print = input('Do you want to print? (yes, no): ')

    # plays game until won
    while not RushHour.game_won():
        # prints gameboard
        if to_print in ['yes', 'y']:
            os.system('cls')
            RushHour.printboard()

        algorithm(RushHour)

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
    car_counter = 0

    # picks a random car until it finds one that can move
    while True:
        # a loop to make sure the algorithm doesn't pick the same car multiple times if it can't move
        car = random.choice(list(RushHour.cars.values()))
        free_space = car.look_around(RushHour)
        distance = 0

        # if a car can move, determine a random distance to move the car
        if free_space['rear'] or free_space['front']:
            while distance == 0:
                distance = random.randrange(free_space['rear'], free_space['front'] + 1)
                
        # heuristic below may cause game to be stuck, so eventually turn it off
        if car_counter < len(RushHour.cars.values()):
            # continues if move is the exact opposite of last move, else breaks
            if len(RushHour.steps) and not (car, - distance) == RushHour.steps[-1] and distance:
                break
        elif distance:
            break

        car_counter += 1

    RushHour.move(car, distance)
    return (car.name, distance)