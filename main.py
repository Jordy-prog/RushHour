import os
from sys import argv

from code.algorithms import bfs_class, hillclimb, random_alg, deepening, bfs_beam, dfs
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
    algorithms = {'1': random_alg.random_pure, '2': random_alg.random_constraint, '3': random_alg.random_branch_and_bound, '4': hillclimb.Hillclimb, '5': bfs_class.bfs, '6': bfs_beam.bfs_beam, '7': deepening.deepening, '8': dfs.dfs}
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
        
        print('Type a number please!')

    # Asks user which algorithm he would like to use
    while not mode == 'manual':
        key = input('Select an algorithm:'
                           '\n1. Purely random'
                           '\n2. Random with constraints'
                           '\n3. Random with brand and bound'
                           '\n4. Hillclimb'
                           '\n5. Breadth first'
                           '\n6. Breadth first with beam search'
                           '\n7. Iterative deepening'
                           '\n8. Depth first\n')

        if key in algorithms:
            algorithm = algorithms[key]
            break

        print('Type a number please!')
    # Run certain algorithm depending on the selections made
    if mode == 'manual':
        manual.manual(RushHour)
    elif mode == 'plot':
        plot.plot(RushHour, algorithm)
    elif algorithm in [random_alg.random_pure, random_alg.random_constraint, random_alg.random_branch_and_bound]:
        random_alg.manager(RushHour, algorithm)
    elif key == "4":
        bfs = bfs_class.bfs(RushHour)
        bfs.run()
    elif key == "5":
        bfs = bfs_class.bfs(RushHour)
        bfs.run(2)
    else:
        algorithm(RushHour)