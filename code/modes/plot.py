from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
from  matplotlib.ticker import FuncFormatter
import pandas as pd

from ..classes import board
from ..algorithms import random, hillclimb, bfs


def plot(RushHour, input_dict):
    '''
    This function runs a certain algorithm a number of times and then plots the data in a graph.
    '''
    stepdata = []

    print(input_dict['algorithm'][0])

    # differentiate between algorithms
    if input_dict['algorithm'][0] in ['1', '2']:
        number_of_runs = 0
    
        # asks user for number of runs
        while number_of_runs <= 0:
            try:
                number_of_runs = int(input('How many times? '))
            except ValueError:
                pass
            
        # run the game a certain times to collect enough data points
        for i in range(number_of_runs):
            RushHour = board.RushHour(input_dict['boardpath'])

            # plays the game
            while not RushHour.game_won():            
                input_dict['algorithm'][1](RushHour)

            stepdata.append(len(RushHour.steps))

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

        print(list(steps_dict.keys()))
        print(steps_dict.values())
        
        # specify properties of bar plot
        plt.bar(list(steps_dict.keys()), steps_dict.values(), color='g')
        plt.xticks(rotation=45)
        plt.xlabel ('Category')
        plt.ylabel ('Frequency')
        plt.title ('Frequency of moved cars')
        plt.text(0.65, 0.9, f'Average steps: {avg_steps} \n Number of runs: {number_of_runs}', transform=plt.gca().transAxes)
        plt.show()

    elif input_dict['algorithm'][0] == '3':
        # runs algorithm and retrieves plotdata
        plotting_data = input_dict['algorithm'][1]()
        info_dict = plotting_data.pop(0) #slices, improvements, runtimes

        slices_amount = info_dict['slices']
        improvements_amount = info_dict['improvements']
        runtime_amount = info_dict['runtimes']

        for plot_data in plotting_data:
            initial_steps = plot_data['initial']
            elimination = plot_data['elimination']
            stepdata = []

            del plot_data['initial']

            for key in plot_data:
                stepdata.append(plot_data[key])

            plt.plot(list(plot_data.keys()), stepdata)

        plt.xticks(rotation=45)
        plt.locator_params(integer=True)
        plt.ylabel('Steps to solve game')
        plt.xlabel('# of slices')
        plt.title ('Hillclimbing with selective elimination')
        plt.text(0.75, 0.75, f'Slices: {slices_amount} \
            \nImprovements: {improvements_amount} \
            \n# of runs: {runtime_amount}', transform=plt.gca().transAxes)
        plt.show()

            

        


        

    # # INFORMATIE HILLCLIMB
    # # Variabelen: Aantal slices, aantal improvements per slice,
    # # In de plot de overgang van lengte van de oplossing.
    # # 1 oplossing, dan de selectieve eleminatie en dan het slicen.
    # Elimination is de eliminatie stap 
    # alle slices hebben nummer van de slice als key en de huidige van de movelijst als value