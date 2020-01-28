import copy
from math import sqrt
from sys import argv
import time

import matplotlib.pyplot as plt

from ..algorithms import random_alg, hillclimb, helpers


class Plot():
    """A class which has several methods to plot the results of different algorithms 
        with MatPlotLib.

    The contained methods are as follows:
        __init__: Intialize variables.
        plot_selector: Manages which plot method to call.
        random_bar: Creates a bar plot for the pure random and contraint random algorithm.
        branchbound_plot: Creates a line graph of the brand & bound random algorithm.
        hillclimb_plot: Creates a line graph of the progression when the hillclimbing
            algorithm is applied.
    """

    def __init__(self, RushHour, algorithm):
        """Initializes variables.
        
        Parameters:
            RushHour (object): The Rush Hour game board object.
            algorithm (function): The algorithm function name.
        """
        self.algorithm = algorithm
        self.elapsed_time_list = []
        self.stepdata = []
        self.board = argv[1]
        self.RushHour_initial = RushHour
        self.best_solution = []

        self.plot_selector()

    def plot_selector(self):
        """A method to decide which plot function to call and run."""
        if self.algorithm in [random_alg.random_pure, random_alg.random_constraint]:
            self.random_bar()
        if self.algorithm == random_alg.random_branch_and_bound:
            self.branchbound_plot()
        elif self.algorithm == hillclimb.Hillclimb:
            self.hillclimb_plot()

    def random_bar(self):
        """Creates a bar plot for the pure random and contraint random algorithm."""
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
            
            # log the steps taken for this round and update best solution if necessary
            self.stepdata.append(len(RushHour_copy.steps))
            if not self.best_solution or len(RushHour_copy.steps) < len(self.best_solution):
                self.best_solution = RushHour_copy.steps 

            # Log the elapsed time
            elapsed_time = (time.time() - start_time)
            self.elapsed_time_list.append(elapsed_time) 

        # write the steps for the best solution to csv
        helpers.write_csv(self.best_solution)

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
        """Creates a line graph of the brand & bound random algorithm."""
        step_dict_list = []
        elapsed_time_list = []
        amount_to_run = int(input("How many times to run (plot)? "))

        start_time = time.time()
        step_dict = random_alg.manager(self.RushHour_initial, self.algorithm)
        elapsed_time_list.append(time.time() - start_time)
        step_dict_list.append(step_dict[0])
        improvements_amount = step_dict[1]
        
        for i in range(amount_to_run - 1):
            start_time = time.time()
            step_dict = random_alg.random_branch_and_bound(self.RushHour_initial, improvements_amount)
            elapsed_time_list.append(time.time() - start_time)
            step_dict_list.append(step_dict)

        total_time = 0
        
        for timed_run in elapsed_time_list:
            total_time += timed_run
        
        avg_time = round(total_time / len(elapsed_time_list), 2)

        decline_sum = 0

        # Calculate the aggregated decline percentage
        for data in step_dict_list:
            initial = list(data.keys())[0]
            final = list(data.keys())[-1]
            decline_sum += ((data[initial] - data[final]) / data[initial]) * 100
        
        avg_decline = round(decline_sum / amount_to_run, 2)

        # Initialize variable with a large number, to determine lowest value in graph
        smallest_endpoint = 9999

        for plot_data in step_dict_list:
            final_value = list(plot_data.keys())[-1]

            if plot_data[final_value] < smallest_endpoint:
                smallest_endpoint = plot_data[final_value]

            plt.plot(list(plot_data.keys()), list(plot_data.values()))

        # Annotate only the smallest ending point of all plotted lines
        plt.annotate(smallest_endpoint, (list(plot_data.keys())[-1], smallest_endpoint),
            textcoords="offset points", xytext=(10,0), ha='center')
            
        # Specify properties of MatPlotLib bar plot
        ticks = [x for x in range(0, len(plot_data), 2)]
        plt.xticks(ticks, rotation=90)
        plt.title (f'{self.board}: Random with branch and bound')
        plt.ylabel('Steps to solve game')
        plt.xlabel('# of improvements')
        plt.text(0.75, 0.75, f'Iterations: {improvements_amount} \
            \n# of runs: {amount_to_run} \
            \nAverage decline: {avg_decline}% \
            \nAverage runtime: {avg_time} seconds', transform=plt.gca().transAxes)
            
        plt.show()

    def hillclimb_plot(self):
        """Creates a line graph of the progression when the hillclimbing
            algorithm is applied.
        """
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
        plt.xlabel('# of improvements')
        plt.text(0.75, 0.75, f'Iterations: {improvements_amount} \
            \n# of runs: {runtime_amount} \
            \nAverage decline: {avg_decline}% \
            \nAverage runtime: {avg_runtime} seconds', transform=plt.gca().transAxes)
        plt.show()