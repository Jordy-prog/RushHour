import copy
import os
import random
from sys import argv
from time import sleep

from .random import random_constraint
from ..classes import board


def hillclimb():
    # asks user how many times the algorithm should try to improve amount of moves
    slices, improvements, runtimes = 0, 0, 0
    
    while slices <= 0 or improvements <= 0 or runtimes <= 0:
        try:
            slices = int(input('Slices? '))
            improvements = int(input('Improvements per slice? '))
            runtimes = int(input('Times to run? '))
        except ValueError:
            pass

    info_dict = {'slices': slices, 'improvements': improvements, 'runtimes': runtimes}
    plotting_data = [info_dict]

    # runs the hillclimber a certain amount of times
    for i in range(runtimes):
        boardstates = []
        plot_data = {}
        RushHour_initial = board.RushHour(f'data/{argv[1]}')

        # do a random run and save the moves that were done
        while not RushHour_initial.game_won():
            move = random_constraint(RushHour_initial)
            boardstates.append(move + (str(RushHour_initial.matrix),))

        plot_data['initial'] = len(boardstates)
        print('length:', len(boardstates))
        slice_times = 0

        while slice_times < slices:
            slice_times += 1
            print('slice:', slice_times)
            first_slice = 0
            last_slice = 0
            
            # take a sequence that is smaller than ~10% of the length of the current solution
            while last_slice - first_slice <= 0 or last_slice - first_slice > (len(boardstates) // 8):
                first_slice = random.randrange(0, len(boardstates))
                last_slice = random.randrange(first_slice, len(boardstates))
                
            sequence = boardstates[first_slice:last_slice]
            boardstates_goal = {}

            # create a dictionary of all possible boardstates that may be achieved for easy lookup
            for step in boardstates[last_slice:]:
                boardstates_goal[step[2]] = (step[0], step[1], step[2])

            RushHour_template = board.RushHour(f'data/{argv[1]}')

            for boardstate in boardstates[:first_slice + 1]:
                RushHour_template.move(RushHour_template.cars[boardstate[0]], boardstate[1])

            improvement_times = 0

            while improvement_times < improvements:
                improvement_times += 1
                RushHour_new = copy.deepcopy(RushHour_template)
                boardstates_new = [sequence[0]]

                while not boardstates_new[-1][2] in boardstates_goal and len(boardstates_new) < len(sequence):
                    move = random_constraint(RushHour_new)
                    boardstates_new.append(move + (str(RushHour_new.matrix),))

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

        # cut that shit
        for i, boardstate in enumerate(boardstates):
            first = i

            for j, check in enumerate(boardstates[i + 1:], 1):
                if check[2] == boardstate[2]:
                    last = i + j
                    del boardstates[first:last]
                    break

        plot_data['elimination'] = len(boardstates)
        print(len(boardstates))
        plotting_data.append(plot_data)
        
    return plotting_data

    # alle boardstates na slice van list in dictionary opslaan
    # dictionary met indexes van lijst voor het filteren van dubbele moves
    # selectieve eliminatie moet dan voor slicing!!