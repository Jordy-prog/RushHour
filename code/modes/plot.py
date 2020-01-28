import copy
from math import sqrt
from sys import argv
import time

import matplotlib.pyplot as plt

from ..algorithms import random_alg, hillclimb, dfs


def plot(RushHour_initial, algorithm):
    """This function runs a certain algorithm a number of times and then plots the data 
        in a MatPlotLib graph.
    
    Parameters:
        RushHour_initial (object): The initial RushHour board object.
        algorithm (function): The algorithm variation to use and visualize with MatPlotLib.

    Output:
        Generates a MatPlotLib graph.
    """
    # Initialize variables
    elapsed_time_list = []
    stepdata = []
    board = argv[1]

    # Differentiate between algorithms
    if algorithm in [random_alg.random_pure, random_alg.random_constraint]:
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

            RushHour = copy.deepcopy(RushHour_initial)

            # Plays the game until won
            while not RushHour.game_won():            
                algorithm(RushHour)
            
            stepdata.append(len(RushHour.steps))
    
            # Log the elapsed time
            elapsed_time = (time.time() - start_time)
            elapsed_time_list.append(elapsed_time) 

        # Initialize the total runtime (seconds)
        total_time = 0
        
        # Calculate the total runtime 
        for timed_run in elapsed_time_list:
            total_time += timed_run
        
        # Calculate averages
        avg_time = round(total_time / len(elapsed_time_list), 2)
        avg_steps = round(sum(stepdata) / len(stepdata), 0)

        sorted_steps = sorted(stepdata)
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
        plt.title(f'{board}: Frequency of moved cars')
        plt.text(0.70, 0.9, f'Average steps: {avg_steps} \
            \nNumber of runs: {number_of_runs} \
            \nAverage runtime: {avg_time} seconds', transform=plt.gca().transAxes)
        plt.show()
    elif algorithm == hillclimb.Hillclimb:
        hillclimber = hillclimb.Hillclimb(RushHour_initial)

        # Runs algorithm and retrieves plotdata
        plotting_data = hillclimber.run()

        # Store information variables in a seperate dictionary
        info_dict = plotting_data.pop(0) 

        print(info_dict)

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
            stepdata = []
            del plot_data['initial']

            # Store the steps in the stepdata list variable
            for key in plot_data:
                stepdata.append(plot_data[key])

                # Determine which plotted point is the smallest, to annotate in the graph
                if key == 'elimination':
                    if plot_data[key] < smallest_endpoint:
                        smallest_endpoint = plot_data[key]

            plt.plot(list(plot_data.keys()), list(plot_data.values()))

        # Annotate only the smallest ending point of all plotted lines
        plt.annotate(smallest_endpoint, (list(plot_data.keys())[-1], smallest_endpoint),
            textcoords="offset points", xytext=(10,0), ha='center')
            
        # Specify properties of MatPlotLib bar plot
        xticks = [str(x) for x in range(2, len(plot_data), 2)] +['elimination']
        print(xticks)
        plt.xticks(xticks, rotation=90)
        # plt.locator_params(integer=True)
        plt.title (f'{board}: Hillclimbing with selective elimination')
        plt.ylabel('Steps to solve game')
        plt.xlabel('# of slices')
        plt.text(0.75, 0.75, f'Iterations: {improvements_amount} \
            \n# of runs: {runtime_amount} \
            \nAverage decline: {avg_decline}% \
            \nAverage runtime: {avg_runtime} seconds', transform=plt.gca().transAxes)
        plt.show()
    elif algorithm == dfs.dfs:
        number_of_runs = 0
    
        # Asks user for number of runs
        while number_of_runs <= 0:
            try:
                number_of_runs = int(input('How many times? '))
            except ValueError:
                pass
            
        # Run the game a certain times to collect enough data points
        for i in range(number_of_runs):
            plotting_data = algorithm(RushHour_initial)

            # Extract tuple data with list enumeration
            x_list = [data[0] for data in plotting_data]
            y_list = [data[1] for data in plotting_data]
            
            # Plot each run
            plt.plot(x_list, y_list, color='g')

        # Specify properties of MatPlotLib bar plot
        plt.xticks(rotation=30)
        plt.xlabel('X data')
        plt.ylabel('Y data')
        plt.title(f'{board}: Frequency of moved cars')
        plt.text(0.65, 0.9, f'Average steps: {avg_steps} \
            \nNumber of runs: {number_of_runs} \
            \nAverage runtime: {avg_time} seconds', transform=plt.gca().transAxes)
        plt.show()