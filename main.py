from code.algorithms import random
from code.classes import board
from math import sqrt
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
    algorithm = None
    to_print = None

    while mode not in ['manual', 'plot', 'test']:
        mode = input('Select a mode (manual, plot, test): ')

    while algorithm not in ['1', '2'] and not mode == 'manual':
        algorithm = input('Select an algorithm: \
                           \n1. Purely random \
                           \n2. Random with constraints \n')

    while to_print not in ['yes', 'no'] and mode == 'test':
        to_print = input('Do you want to print? (yes, no): ')

    board_path = f'data/{argv[1]}'
    rush = board.RushHour(board_path)

    if mode == 'manual':
        steps = 0
        while not rush.game_won(steps):
            os.system('cls')
            rush.printboard()
            print('Moves:', steps)
            car_to_move = input('Which car do you want to move? ').upper()

            if not car_to_move.upper() in rush.cars.keys():
                print('Invalid car!')
                sleep(1)
                continue

            try:
                distance = int(input('How far? '))
            except ValueError:
                print('Invalid distance!')
                sleep(1)
                continue

            if not rush.move(rush.cars[car_to_move], distance):
                print('Invalid move!')
                sleep(1)
            else:
                steps += 1
    elif mode == 'plot':
        stepdata = []

        for i in range(100):
            rush = board.RushHour(board_path)
            steps = 0

            while not rush.game_won(steps):
                steps += 1
                
                if algorithm == '1':
                    random.random_pure(rush)
                elif algorithm == '2':
                    random.random_constraint(rush)

            stepdata.append(steps)

        avg_steps = round(sum(stepdata) / len(stepdata), 0)
        sorted_steps = sorted(stepdata)

        steps_dict = {}

        # determine the width of each bracket in the bar plot
        range_list = max(sorted_steps) - min(sorted_steps)
        bracket_width = int(range_list / sqrt(len(sorted_steps)))

        # categorize the amount of steps with a dictionary structure
        for step in sorted_steps:
            dict_bracket = int(step / bracket_width)
            dict_bracket = f'{min(sorted_steps) + dict_bracket * bracket_width}' + " to " + f'{min(sorted_steps) + dict_bracket * bracket_width + bracket_width}'
            if dict_bracket in steps_dict:
                steps_dict[dict_bracket] += 1
            else:
                steps_dict[dict_bracket] = 1 
        
        # specify properties of bar plot
        plt.bar(list(steps_dict.keys()), steps_dict.values(), color='g')
        plt.xticks(rotation=45)
        plt.xlabel ('Category')
        plt.ylabel ('Frequency')
        plt.title ('Frequency of moved cars')
        plt.text(0.65, 0.9, f'Average steps: {avg_steps}', transform=plt.gca().transAxes)
        plt.show()
    else:
        steps = 0

        while not rush.game_won(steps):
            if to_print == 'yes':
                os.system('cls')
                rush.printboard()

            steps += 1

            if algorithm == '1':
                random.random_pure(rush)
            elif algorithm == '2':
                random.random_constraint(rush)