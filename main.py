import os
from sys import argv

from code.algorithms import hillclimb, random_alg, iterative_deepening, branch_bound, breadth_first
from code.classes import board
from code.modes import create_board, manual, plot


if __name__ == '__main__':
    # Initializing inputs and algorithms dictionary
    modes = {'1': 'manual', '2': 'plot', '3': 'single_run', '4': 'create_board'}
    algorithms = {'1': random_alg.random_pure, '2': random_alg.random_constraint, '3': random_alg.random_branch_and_bound, '4': hillclimb.Hillclimb, '5': breadth_first.BreadthFirst, '6': breadth_first.BreadthFirst, '7': iterative_deepening.IterativeDeepening, '8': branch_bound.BranchAndBound}
    mode = None

    # Asks user for a mode in which program should be run
    while True:
        key = input('Select a mode:' 
                            '\n1. Manual' 
                            '\n2. Plot'
                            '\n3. Single run'
                            '\n4. Create a board\n')
        
        if key in modes:
            mode = modes[key]
            break
        
        print('Type a number please!')

    if not mode == 'create_board':
        # Checks if a filename is given by the user
        if len(argv) < 2:
            print('Usage: python main.py "filename"')
            exit()

        # Checks if file exists and initiate RushHour game
        if not os.path.isfile(f'data/{argv[1]}'):
            print('Could not open file')
            exit()

        RushHour = board.RushHour(f'data/{argv[1]}')
    
    # Asks user which algorithm he would like to use
    while mode in ['plot', 'single_run']:
        text = 'Select an algorithm:' \
                '\n1. Purely random' \
                '\n2. Random with constraints' \
                '\n3. Random with branch and bound' \
                '\n4. Hillclimb\n'
                
        if mode == "single_run":
            text += '5. Breadth first' + \
                    '\n6. Breadth first: beam search' + \
                    '\n7. Iterative deepening' + \
                    '\n8. Depth first: branch and bound\n'

        key = input(text)

        if key in algorithms:
            algorithm = algorithms[key]
            break

        print('Type a number please!')
        
    # Run certain algorithm depending on the selections made
    if mode == 'manual':
        manual.manual(RushHour)
    elif mode == 'create_board':
        create_board.create_board()
    elif mode == 'plot':
        plot.Plot(RushHour, algorithm)
    elif key in ["1", "2", "3"]:
        random_alg.manager(RushHour, algorithm)
    elif key == "4":
        hillclimber = hillclimb.Hillclimb(RushHour)
        hillclimber.run()
    elif key == "5":
        bfs = breadth_first.BreadthFirst(RushHour, beam=None)
        bfs.run()
    elif key == "6":
        beam = input("How long should the beam be: ")

        while not beam and not beam.isdigit():
            beam = input("How long should the beam be: ")

        bfs = breadth_first.BreadthFirst(RushHour, int(beam))
        bfs.run()
    elif key == "7":
        idp = iterative_deepening.IterativeDeepening(RushHour)
        idp.run()
    elif key == "8":
        bnb = branch_bound.BranchAndBound(RushHour)
        bnb.run()