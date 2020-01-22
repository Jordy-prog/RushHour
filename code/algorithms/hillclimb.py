import copy
import os
import random
from sys import argv
import time

from .random import random_constraint
from ..classes import board


def hillclimb(RushHour):
    '''
    Algorithm that generates a random solution and tries to improve it.
    This is done by continously taking sequences out of the solution and try to shorten them, using random moves.
    Also, double boardstates and the moves in between are being removed at the end by selective elimination.
    '''
    # initialize paramaters according to upcoming while condition
    slices, max_slice_size, improvements, runtimes = 0, 21, 0, 0
    
    # requests user input for algorithm parameters
    while slices <= 0 or improvements <= 0 or runtimes <= 0 or max_slice_size > 20:
        try:
            slices = int(input('Slices? '))
            max_slice_size = int(input('What size of slice? '))
            improvements = int(input('Improvements per slice? '))
            runtimes = int(input('Times to run? '))
        except ValueError:
            pass

    info_dict = {'slices': slices, 'slice_size': max_slice_size, 'improvements': improvements, 'runtimes': runtimes}
    plotting_data = [info_dict]
    elapsed_time_list = []

    # runs the hillclimber a certain amount of times
    for i in range(runtimes):

        # time the execution of each run
        start_time = time.time()

        boardstates = []
        plot_data = {}
        RushHour_initial = copy.deepcopy(RushHour)

        # do a random run and save the moves that were done
        while not RushHour_initial.game_won():
            move = random_constraint(RushHour_initial)
            boardstates.append(move + (str(RushHour_initial.matrix),))

        plot_data['initial'] = len(boardstates)
        print('length:', len(boardstates))
        slice_times = 0

        # take slices out of solution and try to improve them
        while slice_times < slices:
            slice_times += 1
            print('slice:', slice_times)
            first_slice = 0
            last_slice = 0
            
            # take a sequence that is smaller than the maximum slice size
            while last_slice - first_slice <= 0 or last_slice - first_slice > max_slice_size:
                first_slice = random.randrange(0, len(boardstates) // 2)
                last_slice = random.randrange(first_slice + 1, len(boardstates))
                
            sequence = boardstates[first_slice:last_slice]
            boardstates_goal = {}

            # create a dictionary of all possible boardstates that may be achieved for easy lookup
            for step in boardstates[last_slice:]:
                boardstates_goal[step[2]] = (step[0], step[1], step[2])

            RushHour_template = copy.deepcopy(RushHour)

            # bring boardstate in starting condition
            for boardstate in boardstates[:first_slice + 1]:
                RushHour_template.move(RushHour_template.cars[boardstate[0]], boardstate[1])

            improvement_times = 0

            # try to improve the same slice a number of times, using random moves
            while improvement_times < improvements:
                improvement_times += 1
                RushHour_new = copy.deepcopy(RushHour_template)
                boardstates_new = [sequence[0]]

                # improve the sequence using random moves
                while not boardstates_new[-1][2] in boardstates_goal and len(boardstates_new) < len(sequence):
                    move = random_constraint(RushHour_new)
                    boardstates_new.append(move + (str(RushHour_new.matrix),))

                # if sequence is improved, replace it with old sequence in original solution
                if len(boardstates_new) < len(sequence):
                    start = first_slice
                    finish = boardstates.index(boardstates_goal[boardstates_new[-1][2]]) + 1
                    del boardstates[start:finish]
                    print('Improved')
                    
                    for i, boardstate in enumerate(boardstates_new):
                        boardstates.insert(first_slice + i, boardstate)

                    break

            plot_data[str(slice_times)] = len(boardstates)
            print(len(boardstates))

            elapsed_time = (time.time() - start_time)
            elapsed_time_list.append(elapsed_time) 

        total_time = 0
        
        for timed_run in elapsed_time_list:
            total_time += timed_run
        
        avg_time = round(total_time / len(elapsed_time_list), 2)
        info_dict['avg_runtime'] = avg_time

        boardstates_indexes = {}

        # selective elimination of double boardstates
        i = 0
        
        while i < len(boardstates):
            if boardstates[i][2] in boardstates_indexes:
                first = boardstates_indexes[boardstates[i][2]]
                last = i
                del boardstates[first:last]
                i = first

                for key in list(boardstates_indexes.keys())[first + 1:last]:
                    del boardstates_indexes[key]
            else:
                boardstates_indexes[boardstates[i][2]] = boardstates.index(boardstates[i])

            i += 1

        plot_data['elimination'] = len(boardstates)
        print('initial:', plot_data['initial'])
        print('finally:', len(boardstates))
        plotting_data.append(plot_data)
        


    return plotting_data

    # alle boardstates na slice van list in dictionary opslaan
    # dictionary met indexes van lijst voor het filteren van dubbele moves
    # selectieve eliminatie moet dan voor slicing!!