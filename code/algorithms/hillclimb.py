import copy
import time

from .helpers import elimination, write_csv
from .random_alg import random_constraint


class Hillclimb():
    """Algorithm that generates a random solution and tries to improve it.
    This is done by continously taking sequences out of the solution and trying to shorten them, 
        using random moves.
    Also, double boardstates and the moves in between are being removed at the end by selective 
        elimination.

    Methods:
        __init__: Initialize class parameters and request user input.
        run: Run the algorithm a certain amount of times and time each duration.
        random_run: Do a random run and save the moves that were done.
        improve: Try to improve the current solution using random moves.
        time: Calculate the average time of all runs.
    """

    def __init__(self, RushHour):
        """Initialize class parameters and request user input.
        
        Parameters:
            RushHour (object): The initial RushHour board object.
        """
        self.iterations, self.runtimes = 0, 0
        
        while self.iterations <= 0 or self.runtimes <= 0:
            try:
                self.iterations = int(input('Number of iterations? '))
                self.runtimes = int(input('Times to run? '))
            except ValueError:
                pass

        self.info_dict = {'iterations': self.iterations, 'runtimes': self.runtimes}
        self.plotting_data = [self.info_dict]
        self.plot_data = {}
        self.elapsed_time_list = []
        self.movelist = []
        self.best_solution = []
        self.RushHour = RushHour

    def run(self):
        """Run the algorithm a certain amount of times and time each duration.

        Returns:
            plotting_data (list): List of all the data that is needed for the plots.
        """
        for i in range(self.runtimes):
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

            if not self.best_solution or len(self.movelist) < len(self.best_solution):
                self.best_solution = []
                for move in self.movelist:
                    self.best_solution.append((move["car"], move["distance"]))

            print('Initial:', self.plot_data['initial'])
            print('After hillclimb:', self.plot_data[str(iteration)])
            print('After elimination:', self.plot_data['elimination'])

        self.time()
        write_csv(self.best_solution)
        return self.plotting_data

    def random_run(self):
        """Do a random run and save the moves that were done."""
        RushHour_random = copy.deepcopy(self.RushHour)
        self.movelist = []

        while not RushHour_random.game_won():
            move = random_constraint(RushHour_random)
            self.movelist.append({'matrix': str(RushHour_random.matrix), 
                            'car': move[0], 
                            'distance': move[1]})

        self.plot_data['initial'] = len(self.movelist)

    def improve(self):
        """Try to improve the current solution using random moves.
        Uses a dictionary of all upcoming boardstates for comparing.
        """
        RushHour_new = copy.deepcopy(self.RushHour)
        movelist_new = []
        boardstates_goal = {}

        # Create dictionary of all upcoming boardstates
        for move in self.movelist[1:]:
            boardstates_goal[move['matrix']] = move

        # Try to improve movelist
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
        """Calculate the average time of all runs."""
        total_time = 0
        
        for timed_run in self.elapsed_time_list:
            total_time += timed_run
        
        avg_time = round(total_time / len(self.elapsed_time_list), 2)
        self.info_dict['avg_runtime'] = avg_time