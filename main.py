from code.algorithms import random
from code.classes import board
from code.modes import *
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
        plot.plot(rush)
    else:
        test.test