import os
from code.algorithms import random


def test(RushHour, algorithm):
    steps = 0

    while not RushHour.game_won(steps):
        steps += 1

        if to_print == 'yes':
            os.system('cls')
            RushHour.printboard()

        if algorithm == '1':
            random.random_pure(RushHour)
        elif algorithm == '2':
            random.random_constraint(RushHour)