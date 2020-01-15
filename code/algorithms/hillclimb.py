import copy
import os
import random
from sys import argv
from time import sleep

from .random import random_constraint
from ..classes import board


# def hillclimb(RushHour_initial, input_dict):
#     boardstates = []
#     plot_data = {}

#     # do one random run and save the moves that were done
#     while not RushHour_initial.game_won():
#         random_constraint(RushHour_initial)
#         boardstates.append(copy.deepcopy(RushHour_initial.matrix))

#     plot_data['initial'] = len(boardstates)
#     print(len(boardstates))

#     # cut that shit
#     for i, boardstate in enumerate(boardstates):
#         indexes = list(j for j, check in enumerate(boardstates[i + 1:], 1) if str(check) == str(boardstate))
#         print(len(boardstates))

#         if indexes:
#             first = i
#             last = i + indexes[-1]
#             del boardstates[first:last]

#     plot_data['elimination'] = len(boardstates)
#     print(len(boardstates))
#     slice_times = 0

#     while slice_times < input_dict['slices']:
#         slice_times += 1
#         print('slice:', slice_times)
#         first_slice = random.randrange(0, len(boardstates)//2)
#         last_slice = random.randrange(len(boardstates)//2, len(boardstates))
#         boardstates_initial = copy.deepcopy(boardstates[first_slice:last_slice])
#         RushHour_template = board.RushHour(f'data/{argv[1]}')
#         RushHour_template.matrix = copy.deepcopy(boardstates_initial[0])

#         for row in RushHour_template.matrix:
#             for car in row:
#                 if car:
#                     RushHour_template.cars[car.name].row = car.row
#                     RushHour_template.cars[car.name].col = car.col

#         improvement_times = 0

#         while improvement_times < input_dict['improvements']:
#             improvement_times += 1
#             RushHour_new = copy.deepcopy(RushHour_template)
#             boardstates_new = [copy.deepcopy(RushHour_new.matrix)]

#             while not str(boardstates_new[-1]) == str(boardstates_initial[-1]) and len(boardstates_new) < len(boardstates_initial):
#                 random_constraint(RushHour_new)
#                 boardstates_new.append(copy.deepcopy(RushHour_new.matrix))

#             if len(boardstates_new) < len(boardstates_initial):
#                 del boardstates[first_slice:last_slice]
#                 print('Improved')
                
#                 for i, boardstate in enumerate(boardstates_new):
#                     boardstates.insert(first_slice + i, boardstate)

#                 break

#         plot_data[str(slice_times)] = len(boardstates)
    
#     print(len(boardstates))
#     return plot_data

def hillclimb(input_dict):
    boardstates_random = {}
    plot_data = {}

    # do 5 random runs, choose the fastest and save the moves that were done
    for i in range(5):
        print(i)
        RushHour_initial = board.RushHour(f'data/{argv[1]}')
        boardstates_random[i] = []

        while not RushHour_initial.game_won():
            # print('hallo')
            move = random_constraint(RushHour_initial)
            boardstates_random[i].append(move + (str(RushHour_initial.matrix),))
        
        if i and len(boardstates_random[i]) < len(boardstates_random[i - 1]):
            del boardstates_random[i - 1]

    boardstates = list(boardstates_random.values())[0]
    plot_data['initial'] = len(boardstates)
    print(len(boardstates))
    slice_times = 0

    while slice_times < input_dict['slices']:
        slice_times += 1
        print('slice:', slice_times)
        first_slice = 0
        last_slice = 0
        
        while last_slice - first_slice < (len(boardstates) // 10):
            first_slice = random.randrange(0, len(boardstates) // 2)
            last_slice = random.randrange(len(boardstates) // 2, len(boardstates))
            
        boardstates_initial = boardstates[first_slice:last_slice]
        RushHour_template = board.RushHour(f'data/{argv[1]}')

        for boardstate in boardstates[:first_slice + 1]:
            RushHour_template.move(RushHour_template.cars[boardstate[0]], boardstate[1])

        improvement_times = 0

        while improvement_times < input_dict['improvements']:
            improvement_times += 1
            RushHour_new = copy.deepcopy(RushHour_template)
            boardstates_new = []

            while not len(boardstates_new) or (not boardstates_new[-1][2] == boardstates_initial[-1][2] and len(boardstates_new) < len(boardstates_initial)):
                move = random_constraint(RushHour_new)
                boardstates_new.append(move + (str(RushHour_new.matrix),))

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
