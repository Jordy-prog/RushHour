import copy
import random
import time

from .helpers import elimination
from .random_alg import random_constraint


class Hillclimb():
    """Algorithm that generates a random solution and tries to improve it.
    This is done by continously taking sequences out of the solution and trying to shorten them, 
        using random moves.
    Also, double boardstates and the moves in between are being removed at the end by selective 
        elimination.
    
    Parameters:
        RushHour (object): The initial RushHour board object.

    Returns:
        plotting_data (list): A list with an information dictionary containing (meta) data and 
            a dictionary containing the steps and slices.
    """
    def __init__(self, RushHour):
        # Initialize parameters according to upcoming while condition
        self.iterations, self.runtimes = 0, 0
        
        # Requests user input for algorithm parameters
        while self.iterations <= 0 or self.runtimes <= 0:
            try:
                self.iterations = int(input('Number of iterations? '))
                self.runtimes = int(input('Times to run? '))
            except ValueError:
                pass

        # Initialize information for the plot.py mode
        self.info_dict = {'iterations': self.iterations, 'runtimes': self.runtimes}
        self.plotting_data = [self.info_dict]
        self.plot_data = {}
        self.elapsed_time_list = []

        self.movelist = []
        self.RushHour = RushHour

    def run(self):
        # Runs the hillclimber a certain amount of times
        for i in range(self.runtimes):
            # Time the execution of each run
            start_time = time.time()

            self.plot_data = {}
            self.random_run()
            iteration = 0

            # Try to improve the found solution a number of times, using random moves
            while iteration < self.iterations:
                iteration += 1
                self.improve()
                self.plot_data[str(iteration)] = len(self.movelist)

            elapsed_time = (time.time() - start_time)
            self.elapsed_time_list.append(elapsed_time)
            self.plot_data['elimination'] = elimination(self.movelist)
            self.plotting_data.append(self.plot_data)

        self.time()
            
        return self.plotting_data

    def random_run(self):
        RushHour_random = copy.deepcopy(self.RushHour)

        # Do a random run and save the moves that were done
        while not RushHour_random.game_won():
            move = random_constraint(RushHour_random)
            self.movelist.append({'matrix': str(RushHour_random.matrix), 
                            'car': move[0], 
                            'distance': move[1]})

        self.plot_data['initial'] = len(self.movelist)

    def improve(self):
        RushHour_new = copy.deepcopy(self.RushHour)
        movelist_new = []
        boardstates_goal = {}

        # Create a dictionary of all possible boardstates that may be achieved for easy lookup
        for move in self.movelist[1:]:
            boardstates_goal[move['matrix']] = move

        # Improve the sequence using random moves
        while len(movelist_new) < len(self.movelist):
            move = random_constraint(RushHour_new)
            movelist_new.append({'matrix': str(RushHour_new.matrix), 
                                'car': move[0], 
                                'distance': move[1]})
            last_board = movelist_new[-1]['matrix']

            # If sequence is improved, replace it with old sequence in original solution
            if last_board in boardstates_goal:
                original_last_move = self.movelist.index(boardstates_goal[last_board])

                if len(movelist_new) < len(self.movelist[1:original_last_move]):
                    end = original_last_move
                    del self.movelist[1:end + 1]
    
                    for i, move in enumerate(movelist_new):
                        self.movelist.insert(1 + i, move)

                    break
    
    def time(self):
        # Initialize total_time to store the total run time
        total_time = 0
        
        # Determine total and average time, add it to the info_dict
        for timed_run in self.elapsed_time_list:
            total_time += timed_run
        
        avg_time = round(total_time / len(self.elapsed_time_list), 2)
        self.info_dict['avg_runtime'] = avg_time

    # def elimination(self):
    #     move_indexes = {}
    #     i = 0
        
    #     # Selective elimination of double boardstates
    #     while i < len(self.movelist):
    #         # If boardstate is found multiple times in moveset, delete everything in between
    #         if self.movelist[i]['matrix'] in move_indexes:
    #             first = move_indexes[self.movelist[i]['matrix']]
    #             last = i
    #             del self.movelist[first:last]
    #             i = first

    #             for key in list(move_indexes.keys())[first + 1:]:
    #                 del move_indexes[key]
    #         else:
    #             move_indexes[self.movelist[i]['matrix']] = self.movelist.index(self.movelist[i])
                
    #         i += 1

    #     self.plot_data['elimination'] = len(self.movelist)



# def hillclimb(RushHour):
#     """Algorithm that generates a random solution and tries to improve it.
#     This is done by continously taking sequences out of the solution and trying to shorten them, 
#         using random moves.
#     Also, double boardstates and the moves in between are being removed at the end by selective 
#         elimination.
    
#     Parameters:
#         RushHour (object): The initial RushHour board object.

#     Returns:
#         plotting_data (list): A list with an information dictionary containing (meta) data and 
#             a dictionary containing the steps and slices.
#     """
#     # Initialize parameters according to upcoming while condition
#     iterations, runtimes = 0, 0
    
#     # Requests user input for algorithm parameters
#     while iterations <= 0 or runtimes <= 0:
#         try:
#             iterations = int(input('Number of iterations? '))
#             runtimes = int(input('Times to run? '))
#         except ValueError:
#             print('That is not a valid number!')
#             pass

#     # Dictionary with information for the plot.py mode
#     info_dict = {'iterations': iterations, 'runtimes': runtimes}
#     plotting_data = [info_dict]

#     elapsed_time_list = []

#     # Runs the hillclimber a certain amount of times
#     for i in range(runtimes):
#         # Time the execution of each run
#         start_time = time.time()

#         movelist = []
#         plot_data = {}
#         RushHour_initial = copy.deepcopy(RushHour)

#         # Do a random run and save the moves that were done
#         while not RushHour_initial.game_won():
#             move = random_constraint(RushHour_initial)
#             movelist.append({'matrix': str(RushHour_initial.matrix), 
#                             'car': move[0], 
#                             'distance': move[1]})

#         plot_data['initial'] = len(movelist)
#         # print('length:', len(movelist))

#         iteration = 0

#         # Try to improve the found solution a number of times, using random moves
#         while iteration < iterations:
#             # print('Iteration:', iteration)
#             iteration += 1

#             boardstates_to_reach = movelist[1:]
#             boardstates_goal = {}

#             # Create a dictionary of all possible boardstates that may be achieved for easy lookup
#             for move in boardstates_to_reach:
#                 boardstates_goal[move['matrix']] = move

#             RushHour_new = copy.deepcopy(RushHour)
#             movelist_new = []

#             # Improve the sequence using random moves
#             while len(movelist_new) < len(movelist):
#                 move = random_constraint(RushHour_new)
#                 movelist_new.append({'matrix': str(RushHour_new.matrix), 
#                                     'car': move[0], 
#                                     'distance': move[1]})
#                 last_board = movelist_new[-1]['matrix']

#                 # If sequence is improved, replace it with old sequence in original solution
#                 if last_board in boardstates_goal:
#                     original_last_move = movelist.index(boardstates_goal[last_board])

#                     if len(movelist_new) < len(movelist[1:original_last_move]):
#                         end = original_last_move
#                         del movelist[1:end + 1]
#                         # print('Improved')
                        
#                         for i, move in enumerate(movelist_new):
#                             movelist.insert(1 + i, move)

#                         # print('new_length:', len(movelist))
#                         break

#             plot_data[str(iteration)] = len(movelist)
#         # print(len(movelist))

#         elapsed_time = (time.time() - start_time)
#         elapsed_time_list.append(elapsed_time) 

#         # Initialize total_time to store the total run time
#         total_time = 0
        
#         # Determine total and average time, add it to the info_dict
#         for timed_run in elapsed_time_list:
#             total_time += timed_run
        
#         avg_time = round(total_time / len(elapsed_time_list), 2)
#         info_dict['avg_runtime'] = avg_time

#         move_indexes = {}
#         i = 0
        
#         # # Selective elimination of double boardstates
#         # while i < len(movelist):
#         #     # If boardstate is found multiple times in moveset, delete everything in between
#         #     if movelist[i]['matrix'] in move_indexes:
#         #         first = move_indexes[movelist[i]['matrix']]
#         #         last = i
#         #         del movelist[first:last]
#         #         i = first

#         #         for key in list(move_indexes.keys())[first + 1:]:
#         #             del move_indexes[key]
#         #     else:
#         #         move_indexes[movelist[i]['matrix']] = movelist.index(movelist[i])
                
#         #     i += 1

#         plot_data['elimination'] = len(movelist)
#         # print('initial:', plot_data['initial'])
#         # print('finally:', len(movelist))
#         plotting_data.append(plot_data)
        
#     return plotting_data