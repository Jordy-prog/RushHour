import os

from code.algorithms import random


def test(RushHour, algorithm, to_print):
    '''
    A function that does a single run of an algorithm.
    '''
    steps = 0

    # plays game until won
    while not RushHour.game_won(steps):
        steps += 1

        # prints gameboard
        if to_print == 'yes':
            os.system('cls')
            RushHour.printboard()

        # algorithm selection
        if algorithm == '1':
            random.random_pure(RushHour)
        elif algorithm == '2':
            random.random_constraint(RushHour)