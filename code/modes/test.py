import os
from code.algorithms import random


def test(RushHour):
    steps = 0

    while not rush.game_won(steps):
        steps += 1

        if to_print == 'yes':
            os.system('cls')
            rush.printboard()

        if algorithm == '1':
            random.random_pure(rush)
        elif algorithm == '2':
            random.random_constraint(rush)