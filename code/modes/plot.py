import matplotlib.pyplot as plt
from math import sqrt
from ..classes import board
from ..algorithms import random


def plot(algorithm, board_path, number_of_runs):
    stepdata = []

    # run the game a certain amount to collect enough data points
    for i in range(number_of_runs):
        RushHour = board.RushHour(board_path)
        steps = 0

        # plays the game according to an algorithm
        while not RushHour.game_won(steps):
            steps += 1
            
            # differentiate between algorithms
            if algorithm == '1':
                random.random_pure(RushHour)
            elif algorithm == '2':
                random.random_constraint(RushHour)

        stepdata.append(steps)

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
    plt.xlabel ('Category')
    plt.ylabel ('Frequency')
    plt.title ('Frequency of moved cars')
    plt.text(0.65, 0.9, f'Average steps: {avg_steps}', transform=plt.gca().transAxes)
    plt.show()