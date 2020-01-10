from code.algorithms import random
from code.classes import board
from sys import exit, argv
from time import sleep

import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats
from scipy.stats import norm
import pylab as pl
import statistics
import pandas
from collections import Counter

import chart_studio.plotly



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

        for i in range(1000):
            rush = board.RushHour(board_path)
            # rush.printboard()

            steps = 0

            while not rush.game_won():
                steps += 1

                if not steps % 5:
                    algorithm == 'move'
                else:
                    algorithm == algorithm_input

                if algorithm == 'chain':
                    random.random_chain(rush)
                elif algorithm == 'move':
                    random.random_move(rush)
                elif algorithm == 'jordy':
                    random.random_chain_jordy(rush)

                if to_print == 'yes':
                    os.system('cls')
                    rush.printboard()

            stepdata.append(steps)


        avg_steps = round(sum(stepdata)/len(stepdata),0)
        sorted_steps = sorted(stepdata)

        steps_dict = {}
        range_list = max(sorted_steps) - min(sorted_steps)
        bracket_width = int(range_list / 10) #133

        for step in sorted_steps:
            dict_bracket = int(step / bracket_width)
            dict_bracket = f'{min(sorted_steps) + dict_bracket * bracket_width}' + " to " + f'{min(sorted_steps) + dict_bracket * bracket_width + bracket_width}'
            if dict_bracket in steps_dict:
                steps_dict[dict_bracket] += 1
            else:
                steps_dict[dict_bracket] = 1 
        
        plt.bar(list(steps_dict.keys()), steps_dict.values(), color='g')
        plt.xticks(rotation=45)
        plt.xlabel ('Category')
        plt.ylabel ('Frequency')
        plt.title ('Frequency of moved cars')
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
                random.random_chain(rush)
            elif algorithm == 'move':
                random.random_move(rush)
            elif algorithm == 'jordy':
                random.random_chain_jordy(rush)

            if to_print == 'yes':
                os.system('cls')
                rush.printboard()

        print(steps)