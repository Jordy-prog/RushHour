import os

from code.algorithms import random, hillclimb, bfs


def test(RushHour, input_dict):
    '''
    A function that does a single run of an algorithm.
    '''
    # algorithm selection
    if input_dict['algorithm'][0] in ['1', '2']:
        # plays game until won
        while not RushHour.game_won():
            # prints gameboard
            if input_dict['to_print'] == 'yes':
                os.system('cls')
                RushHour.printboard()
            
            input_dict['algorithm'][1](RushHour)
    elif input_dict['algorithm'][0] == '3':
        input_dict['algorithm'][1](input_dict)
    elif input_dict['algorithm'][0] == '4':
        input_dict['algorithm'][1](RushHour)
            