from math import sqrt
import os
from sys import exit, argv
from time import sleep

from code.classes import board
from code.algorithms import bfs, hillclimb, random, deepening, bfs_beam
from code.modes import manual, plot, test


if __name__ == '__main__':
    # checks if a filename is given by the user
    if len(argv) < 2:
        print('Usage: python main.py "filename"')
        exit()

    input_dict = {}
    input_dict['boardpath'] = f'data/{argv[1]}'

    # checks if file exists
    if not os.path.isfile(input_dict['boardpath']):
        print('Could not open file')
        exit()

    # initializing input variables
    algorithm = 0
    input_dict['mode'] = None
    input_dict['algorithm'] = None
    input_dict['number_of_runs'] = 0
    algorithms_dict = {'1': random.random_pure, '2': random.random_constraint, '3': hillclimb.hillclimb, '4': bfs_beam.bfs_beam, '5': deepening.deepening}

    # asks user for a mode in which program should be run
    while input_dict['mode'] not in ['manual', 'plot', 'test']:
        input_dict['mode'] = input('Select a mode (manual, plot, test): ')

    # asks user which algorithm he would like to use
    while algorithm not in algorithms_dict.keys() and not input_dict['mode'] == 'manual':
        algorithm = input('Select an algorithm: \
                           \n1. Purely random \
                           \n2. Random with constraints \
                           \n3. Hillclimb \
                           \n4. Breadth first \
                           \n5. Iterative deepening')
    
    if algorithm:
        input_dict['algorithm'] = (algorithm, algorithms_dict[algorithm])

    # asks user for number of runs, if plot option was selected
    if input_dict['mode'] == 'plot' and input_dict['algorithm'][0] in ['1', '2']:
        while input_dict['number_of_runs'] <= 0:
            try:
                input_dict['number_of_runs'] = int(input('How many times? '))
            except ValueError:
                pass

    RushHour = board.RushHour(input_dict['boardpath'])

    # run certain algorithm depending on the selections made
    if input_dict['mode'] == 'manual':
        manual.manual(RushHour)
    elif input_dict['mode'] == 'plot':
        plot.plot(RushHour, input_dict)
    else:
        test.test(RushHour, input_dict)