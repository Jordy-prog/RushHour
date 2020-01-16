import copy
import os
import random
from sys import argv
from time import sleep

from .random import random_constraint
from ..classes import board


def hillclimb():
    # asks user how many times the algorithm should try to improve amount of moves
    slices, improvements = 0, 0
    
    while slices <= 0 or improvements <= 0:
        try:
            slices = int(input('Slices? '))
            improvements = int(input('Improvements per slice? '))
        except ValueError:
            pass

    boardstates_random = {}
    plot_data = {}

    # do 5 random runs, choose the fastest and save the moves that were done
    for i in range(5):
        RushHour_initial = board.RushHour(f'data/{argv[1]}')
        boardstates_random[i] = []

        while not RushHour_initial.game_won():
            # print('hallo')
            move = random_constraint(RushHour_initial)
            boardstates_random[i].append(move + (str(RushHour_initial.matrix),))
        
        if i and len(boardstates_random[i]) < len(list(boardstates_random.values())[0]):
            key_to_remove = list(boardstates_random.keys())[0]
            boardstates_random.pop(key_to_remove)
        elif i:
            del boardstates_random[i]

    boardstates = list(boardstates_random.values())[0]
    plot_data['initial'] = len(boardstates)
    print(len(boardstates))
    slice_times = 0

    while slice_times < slices:
        slice_times += 1
        print('slice:', slice_times)
        first_slice = 0
        last_slice = 0
        print('length:', len(boardstates))
        
        while last_slice - first_slice <= (len(boardstates) // 10):
            first_slice = random.randrange(0, len(boardstates) // 2)
            last_slice = random.randrange(len(boardstates) // 2, len(boardstates))

        print('first:', first_slice)
        print('last:', last_slice)
        print()
            
        boardstates_initial = boardstates[first_slice:last_slice]
        RushHour_template = board.RushHour(f'data/{argv[1]}')

        for boardstate in boardstates[:first_slice + 1]:
            RushHour_template.move(RushHour_template.cars[boardstate[0]], boardstate[1])

        improvement_times = 0

        while improvement_times < improvements:
            improvement_times += 1
            RushHour_new = copy.deepcopy(RushHour_template)
            boardstates_new = []

            while not len(boardstates_new) or (not boardstates_new[-1][2] == boardstates_initial[-1][2] and len(boardstates_new) < len(boardstates_initial)):
                move = random_constraint(RushHour_new)
                boardstates_new.append(move + (str(RushHour_new.matrix),))
                # print(boardstates_new[-1][2])
                # print(boardstates_initial[-1][2])

            # print('old:', len(boardstates_initial))
            # print('new:', len(boardstates_new))
            # print()

            if len(boardstates_new) < len(boardstates_initial):
                del boardstates[first_slice:last_slice]
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
    print(plot_data['initial'])
    print(len(boardstates))
    
    return plot_data
