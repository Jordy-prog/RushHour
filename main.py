import os
from sys import argv

from code.algorithms import bfs, hillclimb_new, random, deepening, bfs_beam, dfs
from code.classes import board
from code.modes import manual, plot


if __name__ == '__main__':
    # Checks if a filename is given by the user
    if len(argv) < 2:
        print('Usage: python main.py "filename"')
        exit()

    # Checks if file exists and initiate RushHour game
    if not os.path.isfile(f'data/{argv[1]}'):
        print('Could not open file')
        exit()

    # Initializing inputs and algorithms dictionary, and the gameboard
    RushHour = board.RushHour(f'data/{argv[1]}')
    modes = {'1': 'manual', '2': 'plot', '3': 'single_run'}
<<<<<<< HEAD
    algorithms = {'1': random.random_pure, '2': random.random_constraint, '3': hillclimb_advanced.hillclimb, '4': bfs.bfs, '5': bfs_beam.bfs_beam, '6': deepening.deepening, '7': dfs.dfs}
=======
    algorithms = {'1': random.random_pure, '2': random.random_constraint, '3': hillclimb_new.hillclimb, '4': bfs.bfs, '5': bfs_beam.bfs_beam, '6': deepening.deepening, '7': dfs.dfs}
>>>>>>> bc6c7a61e4d4e4d866f8ebd2d4933587faa09e27
    mode = None

    # Asks user for a mode in which program should be run
    while True:
        key = input('Select a mode:' 
                            '\n1. Manual' 
                            '\n2. Plot'
                            '\n3. Single run\n')
        
        if key in modes:
            mode = modes[key]
            break

    # Asks user which algorithm he would like to use
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

    # Run certain algorithm depending on the selections made
    if mode == 'manual':
        manual.manual(RushHour)
    elif mode == 'plot':
        plot.plot(RushHour, algorithm)
    elif algorithm in [random.random_pure, random.random_constraint]:
        random.manager(RushHour, algorithm)
    else:
        algorithm(RushHour)