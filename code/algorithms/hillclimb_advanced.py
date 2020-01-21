import copy
import os
import random
from sys import argv
from time import sleep

from .random import random_constraint
from ..classes import board


def hillclimb():
    '''
    Algorithm that generates a random solution and tries to improve it.
    This is done by continously taking sequences out of the solution and try to shorten them, using random moves.
    Also, double boardstates and the moves in between are constantly being removed.
    '''
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
        boardstates_initial = []
        boardstates_indexes = {}
        boardstates = {}
        elimination_data = []
        plot_data = {}
        RushHour_initial = board.RushHour(f'data/{argv[1]}')
    
        # do a random run and save the moves that were done
        while not RushHour_initial.game_won():
            move = random_constraint(RushHour_initial)
            boardstates_initial.append(move + (str(RushHour_initial.matrix),))

            # selective elimination of double boardstates
            if str(RushHour_initial.matrix) in boardstates_indexes:
                first = boardstates_indexes[str(RushHour_initial.matrix)]
                last = len(boardstates_initial) - 1
                elimination_data.append(len(boardstates_initial[first:last]))
                del boardstates_initial[first:last]
            else:
                boardstates_indexes[str(RushHour_initial.matrix)] = len(boardstates_initial) - 1

        # create dictionary of solution
        for move in boardstates_initial:
            boardstates[move[2]] = (move[0], move[1], move[2])

        # add plotting data for the plot function
        plot_data['initial'] = len(boardstates) + sum(elimination_data)
        plot_data['elimination'] = len(boardstates)
        print('Length:', len(boardstates))
        slice_times = 0

        # take a sequence out of the solution and try to improve it
        while slice_times < slices:
            slice_times += 1
            print('Slice:', slice_times)
            first_slice = 0
            last_slice = 0
            
            # take a sequence that is smaller than ~10% of the length of the current solution
            while last_slice - first_slice <= 0 or last_slice - first_slice > (len(boardstates) // 8):
                first_slice = random.randrange(0, len(boardstates))
                last_slice = random.randrange(first_slice, len(boardstates))
            
            # save the sequence, including all the boardstates after (to find the right indexes of solutions)
            sequence = list(boardstates.values())[first_slice:]
            boardstates_goal = {}

            # create a dictionary of all possible boardstates that may be achieved for easy lookup
            for step in list(boardstates.values())[last_slice:]:
                boardstates_goal[step[2]] = (step[0], step[1])

            RushHour_template = board.RushHour(f'data/{argv[1]}')

            # bring board in starting boardstate
            for boardstate in list(boardstates.values())[:first_slice + 1]:
                RushHour_template.move(RushHour_template.cars[boardstate[0]], boardstate[1])

            improvement_times = 0

            # try to improve the sequence a number of times
            while improvement_times < improvements:
                improvement_times += 1

                # create a new board to do moves on
                RushHour_new = copy.deepcopy(RushHour_template)
                boardstates_new = [sequence[0]]
                boardstates_new_indexes = {sequence[0][2]: 0}

                # move randomly on the board until one of the possible boardstates is found
                # or the length has exceeded the sequence length
                while not boardstates_new[-1][2] in boardstates_goal and len(boardstates_new) < len(sequence):
                    move = random_constraint(RushHour_new)
                    boardstates_new.append(move + (str(RushHour_new.matrix),))

                    # selective elimination of double boardstates
                    if str(RushHour_new.matrix) in boardstates_new_indexes:
                        first = boardstates_new_indexes[str(RushHour_new.matrix)]
                        last = len(boardstates_new) - 1
                        del boardstates_new[first:last]
                    else:
                        boardstates_new_indexes[str(RushHour_new.matrix)] = len(boardstates_new) - 1

                # if a boardstate is indeed found faster than it previously was, replace old sequence with the new one
                if boardstates_new[-1][2] in boardstates_goal and len(boardstates_new) < sequence.index(boardstates[boardstates_new[-1][2]]) + 1:
                    boardstates_temp = list(boardstates.values())
                    finish = boardstates_temp.index(boardstates[boardstates_new[-1][2]])
                    start = first_slice
                    after_sequence = list(boardstates.values())[finish + 1:]
                    del boardstates_temp[start:]
                    sequence_new = boardstates_temp + boardstates_new + after_sequence
                    boardstates = {}
                    print('Improved')
                    
                    for boardstate in sequence_new:
                        boardstates[boardstate[2]] = (boardstate[0], boardstate[1], boardstate[2])

                    break

            plot_data[str(slice_times)] = len(boardstates)
            print('length after slice:', len(boardstates))

        print('initial length:', plot_data['initial'])
        print('final length:', len(boardstates))
        plotting_data.append(plot_data)
        
    return plotting_data

    # alle boardstates na slice van list in dictionary opslaan
    # dictionary met indexes van lijst voor het filteren van dubbele moves
    # selectieve eliminatie moet dan voor slicing!!
    # voor het slices, moet index weten van boardstate die het geworden is om het te verwijderen, enn dan veranderen weer alle indexes
    # Sla reserve hillclimber op, of zoek terug
    # fix lager dan laagste oplossing gaan
    # test voor grotere borden