from math import sqrt
import os
from sys import exit, argv
from time import sleep

from code.classes import board
from code.modes import manual, plot, test


if __name__ == '__main__':
    if len(argv) < 2:
        print('Usage: python main.py "filename"')
        exit()

    mode = None
    algorithm = None
    to_print = None

    while mode not in ['manual', 'plot', 'test']:
        mode = input('Select a mode (manual, plot, test): ')

    while algorithm not in ['1', '2'] and not mode == 'manual':
        algorithm = input('Select an algorithm: \
                           \n1. Purely random \
                           \n2. Random with constraints \n')

    while to_print not in ['yes', 'no'] and mode == 'test':
        to_print = input('Do you want to print? (yes, no): ')

    board_path = f'data/{argv[1]}'
    RushHour = board.RushHour(board_path)

    if mode == 'manual':
        manual.manual(RushHour)
    elif mode == 'plot':
        plot.plot(RushHour, algorithm, board_path)
    else:
        test.test(RushHour, algorithm)