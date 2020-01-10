from code.algorithms import algorithms
from code.classes import board
from sys import exit, argv
from time import sleep


import matplotlib.pyplot as plt
import os



if __name__ == '__main__':
    if len(argv) < 2:
        print('Usage: python main.py "filename"')
        exit()

    mode = None
    algorithm_input = None
    to_print = None

    while mode not in ['manual', 'plot', 'test']:
        mode = input('Select a mode (manual, plot, test): ')

    while algorithm_input not in ['move', 'chain', 'jordy'] and not mode == "manual":
        algorithm_input = input('Select an algorithm (move, chain, jordy): ')

    while to_print not in ['yes', 'no']:
        to_print = input('Do you want to print? (yes, no): ')

    board_path = f'data/{argv[1]}'
    rush = board.RushHour(board_path)
    rush.printboard()
    algorithm = algorithm_input

    if mode == 'manual':
        while not rush.game_won():
            car_to_move = input('Which car do you want to move? ').upper()

            if not car_to_move.upper() in rush.cars.keys():
                print('Unable to move that car in that direction!')
                sleep(1)
                continue

            try:
                distance = int(input('How far? '))
            except ValueError:
                print('Invalid distance')
                sleep(1)
                continue

            if not rush.move(rush.cars[car_to_move], distance):
                print('Too bad sucker')
                sleep(1)

            sleep(2)
            os.system('cls')
            rush.printboard()
    elif mode == 'plot':
        stepdata = []

        for i in range(100):
            rush = RushHour()
            # rush.printboard()

            steps = 0

            while not rush.game_won():
                steps += 1

                if not steps % 5:
                    algorithm == 'move'
                else:
                    algorithm == algorithm_input

                if algorithm == 'chain':
                    algorithms.random_chain(rush)
                elif algorithm == 'move':
                    algorithms.random_move(rush)
                elif algorithm == 'jordy':
                    algorithms.random_chain_jordy(rush)

                if to_print == 'yes':
                    os.system('cls')
                    rush.printboard()

            stepdata.append(steps)
            print(steps)

        plt.plot(stepdata)
        plt.show()
    else:
        steps = 0

        while not rush.game_won():
            steps += 1

            if (steps % 5) == 0:
                algorithm = 'move'
            else:
                algorithm = algorithm_input

            if algorithm == 'chain':
                algorithms.random_chain(rush)
            elif algorithm == 'move':
                algorithms.random_move(rush)
            elif algorithm == 'jordy':
                algorithms.random_chain_jordy(rush)

            if to_print == 'yes':
                os.system('cls')
                rush.printboard()

        print(steps)