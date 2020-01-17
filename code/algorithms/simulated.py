import copy
import os
import random
from sys import argv
from time import sleep

from .random import random_constraint
from ..classes import board


def simulated():
    # asks user how many times the algorithm should try to improve amount of moves
    slices, runtimes = 0, 0
    
    while slices <= 0 or runtimes <= 0:
        try:
            slices = int(input('Slices? '))
            runtimes = int(input('Times to run? '))
        except ValueError:
            pass

    # runs the hillclimber a certain amount of times
    for i in range(runtimes):
        boardstates_random = {}
        plot_data = {}

        # do a number of random runs, choose the fastest and save the moves that were done
        for i in range(5):
            RushHour_initial = board.RushHour(f'data/{argv[1]}')
            boardstates_random[i] = []

            while not RushHour_initial.game_won():
                move = random_constraint(RushHour_initial)
                boardstates_random[i].append(move + (str(RushHour_initial.matrix),))
            
            if i and len(boardstates_random[i]) < len(list(boardstates_random.values())[0]):
                key_to_remove = list(boardstates_random.keys())[0]
                boardstates_random.pop(key_to_remove)
            elif i:
                del boardstates_random[i]

        boardstates = list(boardstates_random.values())[0]
        plot_data['initial'] = len(boardstates)
        print('length:', len(boardstates))
        slice_times = 0

        while slice_times < slices:
            temperature = 1000 * (0.99 ** slice_times)
            slice_times += 1
            print('slice:', slice_times)
            first_slice = 0
            last_slice = 0
            
            while last_slice - first_slice <= (len(boardstates) // 10):
                first_slice = random.randrange(0, len(boardstates) // 2)
                last_slice = random.randrange(len(boardstates) // 2, len(boardstates))
                
            boardstates_initial = boardstates[first_slice:last_slice]
            RushHour_template = board.RushHour(f'data/{argv[1]}')

            for boardstate in boardstates[:first_slice + 1]:
                RushHour_template.move(RushHour_template.cars[boardstate[0]], boardstate[1])

            boardstates_new = [boardstates_initial[0]]

            while not boardstates_new[-1][2] == boardstates_initial[-1][2] and len(boardstates_new) < 10 * len(boardstates_initial):
                move = random_constraint(RushHour_template)
                boardstates_new.append(move + (str(RushHour_template.matrix),))

            if boardstates_new[-1][2] == boardstates_initial[-1][2] and random.random() < chance(len(boardstates_initial), len(boardstates_new), temperature):
                del boardstates[first_slice:last_slice]
                print('Changed')
                
                for i, boardstate in enumerate(boardstates_new):
                    boardstates.insert(first_slice + i, boardstate)

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

def chance(moves_old, moves_new, temperature):
    score_old = 0
    score_new = moves_new / moves_old
    chance = 2 ** ((score_old - score_new) / temperature)
    return chance