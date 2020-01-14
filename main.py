from math import sqrt
import os
from sys import exit, argv
from time import sleep

from code.classes import board
from code.modes import manual, plot, test


if __name__ == '__main__':
    # checks if a filename is given by the user
    if len(argv) < 2:
        print('Usage: python main.py "filename"')
        exit()

    board_path = f'data/{argv[1]}'

    # checks if file exists
    if not os.path.isfile(board_path):
        print('Could not open file')
        exit()

    # initializing input variables
    mode = None
    algorithm = None
    to_print = None
    number_of_runs = 0
    slices = 0
    improvements = 0
    input_dict = {}

    # asks user for a mode in which program should be run
    while mode not in ['manual', 'plot', 'test']:
        input_dict['mode'] = input('Select a mode (manual, plot, test): ')

    # asks user for number of runs, if plot option was selected
    if mode == 'plot':
        while number_of_runs <= 0:
            try:
                number_of_runs = int(input('How many times? '))
            except ValueError:
                pass

    # asks user which algorithm he would like to use
    while algorithm not in ['1', '2', '3', '4'] and not mode == 'manual':
        algorithm = input('Select an algorithm: \
                           \n1. Purely random \
                           \n2. Random with constraints \
                           \n3. Hillclimb \
                           \n4. Breadth first\n')

    # asks user how many times the algorithm should try to improve amount of moves
    if algorithm == '3':
        while slices <= 0 or improvements <= 0:
            try:
                slices = int(input('Slices? '))
                improvements = int(input('Improvements per slice? '))
            except ValueError:
                pass

    # asks user if he wants results to be printed
    while to_print not in ['yes', 'no'] and mode == 'test':
        to_print = input('Do you want to print? (yes, no): ')

    RushHour = board.RushHour(board_path)

    # run certain algorithm depending on the selections made
    if mode == 'manual':
        manual.manual(RushHour)
    elif mode == 'plot':
        plot.plot(algorithm, board_path, number_of_runs)
    else:
        test.test(RushHour, algorithm, to_print, slices, improvements)