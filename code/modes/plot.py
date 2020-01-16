from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
from  matplotlib.ticker import FuncFormatter

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
        # run the game a certain times to collect enough data points
        for i in range(input_dict['number_of_runs']):
            RushHour = board.RushHour(input_dict['boardpath'])

            # plays the game
            while not RushHour.game_won():            
                input_dict['algorithm'][1](RushHour)

            stepdata.append(RushHour.steps)

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

        print(".aaaaaaaaa")
        print(list(steps_dict.keys()))
        print(steps_dict.values())
        
        # specify properties of bar plot
        plt.bar(list(steps_dict.keys()), steps_dict.values(), color='g')
        plt.xticks(rotation=45)
        plt.xlabel ('Category')
        plt.ylabel ('Frequency')
        plt.title ('Frequency of moved cars')
        plt.text(0.65, 0.9, f'Average steps: {avg_steps}', transform=plt.gca().transAxes)
        plt.show()

    elif input_dict['algorithm'][0] == '3':
        # runs algorithm and retrieves plotdata
        plot_data = input_dict['algorithm'][1]()
        #print(plot_data)

        initial_steps = plot_data['initial']
        elimination = plot_data['elimination']
        print(initial_steps, elimination)

        del plot_data['initial']

        for key in plot_data:
            stepdata.append(plot_data[key])

        # print('.....')
        # print(stepdata)
        # print(plot_data)
        # print("ppppppppp")
        print(list(plot_data.keys()))
        print(stepdata)
        print(plot_data.values())

        plt.plot(list(plot_data.keys()), stepdata)
        plt.xticks(rotation=45)
        plt.locator_params(integer=True)
        plt.ylabel('Steps to solve game')
        plt.xlabel('# of slices')
        plt.title ('Hillclimbing with selective elimination')
        plt.text(0.65, 0.9, f'Initital steps: {initial_steps} \n Elimination: {elimination}', transform=plt.gca().transAxes)
        plt.show()
        

        


        

    # # INFORMATIE HILLCLIMB
    # # Variabelen: Aantal slices, aantal improvements per slice,
    # # In de plot de overgang van lengte van de oplossing.
    # # 1 oplossing, dan de selectieve eleminatie en dan het slicen.
    # Elimination is de eliminatie stap 
    # alle slices hebben nummer van de slice als key en de huidige van de movelijst als value