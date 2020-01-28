import copy
from math import sqrt
from sys import argv
import time

import matplotlib.pyplot as plt

from ..algorithms import random_alg, hillclimb, branch_bound

class Plot():
    def __init__(self, RushHour, algorithm):
        self.algorithm = algorithm
        self.elapsed_time_list = []
        self.stepdata = []
        self.board = argv[1]
        self.RushHour_initial = RushHour

        self.plot_selector()

    def plot_selector(self):
        """This function runs a certain algorithm a number of times and then plots the data 
            in a MatPlotLib graph.
        
        Parameters:
            RushHour_initial (object): The initial RushHour board object.
            algorithm (function): The algorithm variation to use and visualize with MatPlotLib.

        Output:
            Generates a MatPlotLib graph.
        """
        if self.algorithm in [random_alg.random_pure, random_alg.random_constraint]:
            self.random_bar()
        if self.algorithm == random_alg.random_branch_and_bound:
            self.branchbound_plot()
        elif self.algorithm == hillclimb.Hillclimb:
            self.hillclimb_plot()


    def random_bar(self):
        number_of_runs = 0

        # Asks user for number of runs
        while number_of_runs <= 0:
            try:
                number_of_runs = int(input('How many times? '))
            except ValueError:
                pass
            
        # Run the game a certain times to collect enough data points
        for i in range(number_of_runs):
            # Time the execution of each run
            start_time = time.time()

            RushHour_copy = copy.deepcopy(self.RushHour_initial)

            # Plays the game until won
            while not RushHour_copy.game_won():            
                self.algorithm(RushHour_copy)
            
            self.stepdata.append(len(RushHour_copy.steps))

            # Log the elapsed time
            elapsed_time = (time.time() - start_time)
            self.elapsed_time_list.append(elapsed_time) 

        # Initialize the total runtime (seconds)
        total_time = 0
        
        # Calculate the total runtime 
        for timed_run in self.elapsed_time_list:
            total_time += timed_run
        
        # Calculate averages
        avg_time = round(total_time / len(self.elapsed_time_list), 2)
        avg_steps = round(sum(self.stepdata) / len(self.stepdata), 0)

        sorted_steps = sorted(self.stepdata)
        steps_dict = {}

        # Determine the range of steps per bar in the plot
        range_list = max(sorted_steps) - min(sorted_steps)
        bracket_width = int(range_list / sqrt(len(sorted_steps)))

        # Categorize the amount of steps with a dictionary structure
        for step in sorted_steps:
            dict_bracket = int(step / bracket_width)
            dict_bracket = f'{min(sorted_steps) + dict_bracket * bracket_width}' + ' to ' + f'{min(sorted_steps) + dict_bracket * bracket_width + bracket_width}'
            
            # Add or set the amount in the steps category
            if dict_bracket in steps_dict:
                steps_dict[dict_bracket] += 1
            else:
                steps_dict[dict_bracket] = 1 

        # Specify properties of MatPlotLib bar plot
        plt.bar(list(steps_dict.keys()), steps_dict.values(), color='g')
        plt.locator_params(integer=True)
        plt.xticks(rotation=30)
        plt.xlabel('Category')
        plt.ylabel('Frequency')
        plt.title(f'{self.board}: Frequency of moved cars')
        plt.text(0.70, 0.9, f'Average steps: {avg_steps} \
            \nNumber of runs: {number_of_runs} \
            \nAverage runtime: {avg_time} seconds', transform=plt.gca().transAxes)
        plt.show()

    def branchbound_plot(self):
        step_dict_list = []
        amount_to_run = int(input("How many times to run (plot)? "))

        step_dict = random_alg.manager(self.RushHour_initial, self.algorithm)
        step_dict_list.append(step_dict[0])
        improvements_amount = step_dict[1]
        
        for i in range(amount_to_run - 1):
            step_dict = random_alg.random_branch_and_bound(self.RushHour_initial, improvements_amount)
            step_dict_list.append(step_dict)

        for item in step_dict_list:
            plt.plot(list(item.keys()), list(item.values()))
            
        plt.show()
        # x as integer
        # avg runtime, lowest point, avg decline, number of runs
        








    def hillclimb_plot(self):
        hillclimber = hillclimb.Hillclimb(self.RushHour_initial)

        # Runs algorithm and retrieves plotdata
        plotting_data = hillclimber.run()

        # Store information variables in a seperate dictionary
        info_dict = plotting_data.pop(0) 

        # Retrieve information variables
        improvements_amount = info_dict['iterations']
        runtime_amount = info_dict['runtimes']
        avg_runtime = info_dict['avg_runtime']

        decline_sum = 0

        # Calculate the aggregated decline percentage
        for data in plotting_data:
            decline_sum += ((data['initial'] - data['elimination']) / data['initial']) * 100
        
        avg_decline = round(decline_sum / runtime_amount, 2)

        # Initialize variable with a large number, to determine lowest value in graph
        smallest_endpoint = 9999

        # Plot each run in graph
        for plot_data in plotting_data:
            if plot_data['elimination'] < smallest_endpoint:
                smallest_endpoint = plot_data['elimination']

            plt.plot(list(plot_data.keys()), list(plot_data.values()))

        # Annotate only the smallest ending point of all plotted lines
        plt.annotate(smallest_endpoint, (list(plot_data.keys())[-1], smallest_endpoint),
            textcoords="offset points", xytext=(10,0), ha='center')
            
        # Specify properties of MatPlotLib bar plot
        ticks = ["initial"] + [str(x) for x in range(2, len(plot_data), 2)] + ["elimination"]
        plt.xticks(ticks, rotation=90)
        
        plt.title (f'{self.board}: Hillclimbing with selective elimination')
        plt.ylabel('Steps to solve game')
        plt.xlabel('# of slices')
        plt.text(0.75, 0.75, f'Iterations: {improvements_amount} \
            \n# of runs: {runtime_amount} \
            \nAverage decline: {avg_decline}% \
            \nAverage runtime: {avg_runtime} seconds', transform=plt.gca().transAxes)
        plt.show()

    def dfs_plot(self):
        number_of_runs = 0

        # Asks user for number of runs
        while number_of_runs <= 0:
            try:
                number_of_runs = int(input('How many times? '))
            except ValueError:
                pass
            
        # Run the game a certain times to collect enough data points
        for i in range(number_of_runs):
            plotting_data = self.algorithm(self.RushHour_initial)

            # Extract tuple data with list enumeration
            x_list = [data[0] for data in plotting_data]
            y_list = [data[1] for data in plotting_data]
            
            # Plot each run
            plt.plot(x_list, y_list, color='g')

        # # Specify properties of MatPlotLib bar plot
        # plt.xticks(rotation=30)
        # plt.xlabel('X data')
        # plt.ylabel('Y data')
        # plt.title(f'{self.board}: Frequency of moved cars')
        # plt.text(0.65, 0.9, f'Average steps: {avg_steps} \
        #     \nNumber of runs: {number_of_runs} \
        #     \nAverage runtime: {avg_time} seconds', transform=plt.gca().transAxes)
        # plt.show()