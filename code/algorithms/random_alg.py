import copy
import os
import random

from . import random_alg


def manager(RushHour, algorithm):
    """Function to manage user interaction. Responsible for printing results and printing
        the game board.
    
    Parameters:
        RushHour (object): The initial RushHour board object.
        algorithm (function): The algorithm variation to run.
    """
    if algorithm == random_alg.random_branch_and_bound:
        times_to_run = 0

        while times_to_run <= 0:
            try:
                times_to_run = int(input('How many times to improve? '))
            except ValueError:
                pass

        return (random_branch_and_bound(RushHour, times_to_run), times_to_run)
    else:
        to_print = None

        # Asks user if he wants results to be printed
        while to_print not in ['yes', 'y', 'no', 'n']:
            to_print = input('Do you want to print? (yes, no): ')

        # Plays game until won
        while not RushHour.game_won():
            # Prints gameboard
            if to_print in ['yes', 'y']:
                os.system('cls')
                RushHour.printboard()

            algorithm(RushHour)

def random_pure(RushHour):
    """Implementation of the pure random algorithm.
    Picks a random car until it finds a car that can move, then moves it.
    
    Parameters:
        RushHour (object): The initial RushHour board object.
    """
    while True:
        car = random.choice(list(RushHour.cars.values()))
        free_space = car.look_around(RushHour)
        
        if free_space['rear'] or free_space['front']:
            break

    distance = random.randrange(free_space['rear'], free_space['front'] + 1)
    RushHour.move(car, distance)

def random_constraint(RushHour):
    """Implements the semi-random contraint algorithm.
    Adds an extra constraint to the 'random_pure' function:
        Makes sure a car can't undo its last move, 
            this is done to prevent the algorithm from just moving a car back and forth.
    
    Parameters:
        RushHour (object): The initial RushHour board object.
    
    Returns:
        (car.name, distance) (tuple): A tuple containing the unique car letter 
            and the amount of spaces it has been moved.
    """
    car_counter = 0

    # Picks a random car until it finds one that can move
    while True:
        car = random.choice(list(RushHour.cars.values()))
        free_space = car.look_around(RushHour)
        distance = 0

        # If a car can move, determine a random distance to move the car
        if free_space['rear'] or free_space['front']:
            while distance == 0:
                distance = random.randrange(free_space['rear'], free_space['front'] + 1)
                
        # Heuristic below may cause game to be stuck, so eventually turn it off
        if car_counter < len(RushHour.cars.values()):
            # Picks a new car if move is the exact opposite of last move, else breaks
            if len(RushHour.steps) and not (car, - distance) == RushHour.steps[-1] and distance:
                break
        elif distance:
            break

        car_counter += 1

    RushHour.move(car, distance)
    return (car.name, distance)

def random_branch_and_bound(RushHour_initial, times_to_run):
    """Runs the random_constraint algorithm multiple times.
    Adds an extra 'branch and bound' heuristic, so it won't accept worse solutions.

    Parameters:
        RushHour_initial (object): The initial RushHour object.
        times_to_run (integer): The amount of times to run the random_constraint algorithm.
    """
    previous_solution = None
    step_list = {}

    for i in range(times_to_run):
        RushHour = copy.deepcopy(RushHour_initial)

        while not RushHour.game_won():
            random_constraint(RushHour)

            if previous_solution and len(RushHour.steps) == previous_solution:
                break
        
        previous_solution = len(RushHour.steps) 
        step_list[i] = previous_solution

    print('Final:', previous_solution)
    print(step_list)

    return step_list