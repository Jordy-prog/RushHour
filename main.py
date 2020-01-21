from math import sqrt
import os
from sys import exit, argv
from time import sleep

from code.classes import board
from code.algorithms import bfs, hillclimb, random, deepening, bfs_beam, dfs
from code.modes import manual, plot, test


if __name__ == '__main__':
    # checks if a filename is given by the user
    if len(argv) < 2:
        print('Usage: python main.py "filename"')
        exit()

    # checks if file exists and initiate RushHour game
    if not os.path.isfile(f'data/{argv[1]}'):
        print('Could not open file')
        exit()
    RushHour = board.RushHour(f'data/{argv[1]}')

    # initializing inputs and algorithms dictionary
    inputs = {}
    algorithms = {'1': random.random_pure, '2': random.random_constraint, '3': hillclimb.hillclimb, '4': bfs.bfs, '5': bfs_beam.bfs_beam, '6': deepening.deepening, '7': dfs.dfs}

    # asks user for a mode in which program should be run
    mode = None
    while mode not in ['manual', 'plot', 'test']:
        mode = input('Select a mode (manual, plot, test): ')

    # asks user which algorithm he would like to use
    while not mode == 'manual':
        key = input('Select an algorithm:'
                           '\n1. Purely random'
                           '\n2. Random with constraints'
                           '\n3. Hillclimb'
                           '\n4. Breadth first'
                           '\n5. Breadth first with beam search'
                           '\n6. Iterative deepening'
                           '\n7. Depth first\n')
        if key in algorithms:
            algorithm = algorithms[key]
            break

    # run certain algorithm depending on the selections made
    if mode == 'manual':
        manual.manual(RushHour)
    elif mode == 'plot':
        plot.plot(RushHour, algorithm)
    elif algorithm in [random.random_pure, random.random_constraint]:
        random.manager(RushHour, algorithm)
    else:
        algorithm(RushHour)

    '''
    State-space: Totale hoeveelheid bordconfiguraties
    Upper-bound: Oneindig (max. aantal moves tot een oplossing)
    Lower-bound: Minimaal aantal stappen tot een oplossing (verschilt per bord)
    Advanced fixen
    Simulated annealing
    hillclimb loop eromheen zetten voor meer runs vanaf start
    breadfirst fixen
    depthfirst implementeren
    ONDERZOEKJE
    slicegrootte aanpassen
    '''