from math import sqrt
import time
import copy

import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter

from ..classes import board
from ..algorithms import random, hillclimb, bfs, dfs


def plot(RushHour_initial, algorithm):
    """
    This function runs a certain algorithm a number of times and then plots the data in a graph.
    """
    elapsed_time_list = []
    stepdata = []

    # differentiate between algorithms
    if algorithm in [random.random_pure, random.random_constraint]:
        number_of_runs = 0
    
        # asks user for number of runs
        while number_of_runs <= 0:
            try:
                number_of_runs = int(input('How many times? '))
            except ValueError:
                pass
            
        # run the game a certain times to collect enough data points
        for i in range(number_of_runs):

            # time the execution of each run
            start_time = time.time()

            RushHour = copy.deepcopy(RushHour_initial)

            # plays the game
            while not RushHour.game_won():            
                algorithm(RushHour)
            
            stepdata.append(len(RushHour.steps))
    
            elapsed_time = (time.time() - start_time)
            elapsed_time_list.append(elapsed_time) 

        total_time = 0
        
        for timed_run in elapsed_time_list:
            total_time += timed_run
        
        
        avg_time = round(total_time / len(elapsed_time_list), 2)
        avg_steps = round(sum(stepdata) / len(stepdata), 0)
        sorted_steps = sorted(stepdata)

        steps_dict = {}

        # determine the width of each bracket in the bar plot
        range_list = max(sorted_steps) - min(sorted_steps)
        bracket_width = int(range_list / sqrt(len(sorted_steps)))

        # categorize the amount of steps with a dictionary structure
        for step in sorted_steps:
            dict_bracket = int(step / bracket_width)
            dict_bracket = f'{min(sorted_steps) + dict_bracket * bracket_width}' + " to " + f'{min(sorted_steps) + dict_bracket * bracket_width + bracket_width}'
            
            # add or set the amount in the steps category
            if dict_bracket in steps_dict:
                steps_dict[dict_bracket] += 1
            else:
                steps_dict[dict_bracket] = 1 

        # specify properties of bar plot
        plt.bar(list(steps_dict.keys()), steps_dict.values(), color='g')
        plt.xticks(rotation=45)
        plt.xlabel('Category')
        plt.ylabel('Frequency')
        plt.title('Frequency of moved cars')
        plt.text(0.65, 0.9, f'Average steps: {avg_steps} \
            \nNumber of runs: {number_of_runs} \
            \nAverage runtime: {avg_time} seconds', transform=plt.gca().transAxes)
        plt.show()

    elif algorithm == hillclimb.hillclimb:
        # runs algorithm and retrieves plotdata
        plotting_data = algorithm(RushHour_initial)
        info_dict = plotting_data.pop(0) #slices, improvements, runtimes

        slices_amount = info_dict['slices']
        improvements_amount = info_dict['improvements']
        runtime_amount = info_dict['runtimes']
        slice_size = info_dict['slice_size']
        avg_runtime = info_dict['avg_runtime']

        decline_sum = 0

        for data in plotting_data:
            decline_sum += ((data['initial'] - data['elimination']) / data['initial']) * 100
        
        avg_decline = round(decline_sum / runtime_amount, 2)

        for plot_data in plotting_data:
            stepdata = []
            del plot_data['initial']

            for key in plot_data:
                stepdata.append(plot_data[key])

            plt.plot(list(plot_data.keys()), list(plot_data.values()))
            # plt.annotate(stepdata[0], (list(plot_data.keys())[0], stepdata[0]),
            # textcoords="offset points", xytext=(0,10), ha='center')
            # plt.annotate(stepdata[-1], (list(plot_data.keys())[-1], stepdata[-1]),
            # textcoords="offset points", xytext=(10,0), ha='center')
            
        plt.xticks(rotation=90)
        plt.locator_params(integer=True)
        plt.title('Hillclimbing with selective elimination')
        plt.ylabel('Steps to solve game')
        plt.xlabel('# of slices')
        plt.text(0.75, 0.75, f'Slices: {slices_amount} \
            \nImprovements: {improvements_amount} \
            \nSlice size: {slice_size}  \
            \n# of runs: {runtime_amount} \
            \nAverage decline: {avg_decline}% \
            \nAverage runtime: {avg_runtime} seconds', transform=plt.gca().transAxes)
        plt.show()
    elif algorithm == dfs.dfs:
        number_of_runs = 0
    
        # asks user for number of runs
        while number_of_runs <= 0:
            try:
                number_of_runs = int(input('How many times? '))
            except ValueError:
                pass
            
        # run the game a certain times to collect enough data points
        for i in range(number_of_runs):
            plotting_data = algorithm(RushHour_initial)
            x_list = [data[0] for data in plotting_data]
            y_list = [data[1] for data in plotting_data]

            plt.plot(x_list, y_list, color='g')
        plt.xticks(rotation=45)
        plt.xlabel('Category')
        plt.ylabel('Frequency')
        plt.title('Frequency of moved cars')
        # plt.text(0.65, 0.9, f'Average steps: {avg_steps} \
        #     \nNumber of runs: {number_of_runs} \
        #     \nAverage runtime: {avg_time} seconds', transform=plt.gca().transAxes)
        plt.show()
            

        


        

    # # INFORMATIE HILLCLIMB
    # # Variabelen: Aantal slices, aantal improvements per slice,
    # # In de plot de overgang van lengte van de oplossing.
    # # 1 oplossing, dan de selectieve eleminatie en dan het slicen.
    # Elimination is de eliminatie stap 
    # alle slices hebben nummer van de slice als key en de huidige van de movelijst als value