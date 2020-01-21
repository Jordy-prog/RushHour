# import os

# from code.algorithms import random, hillclimb, bfs


# def test(RushHour, input_dict):
#     '''
#     A function that does a single run of an algorithm.
#     '''
#     # algorithm selection
#     if input_dict['algorithm'][0] in ['1', '2']:
#         # asks user if he wants results to be printed
#         to_print = None

#         while to_print not in ['yes', 'y', 'no', 'n']:
#             to_print = input('Do you want to print? (yes, no): ')

#         # plays game until won
#         while not RushHour.game_won():
#             # prints gameboard
#             if to_print in ['yes', 'y']:
#                 os.system('cls')
#                 RushHour.printboard()
            
#             input_dict['algorithm'][1](RushHour)
#     else:
#         input_dict['algorithm'][1](RushHour)

            