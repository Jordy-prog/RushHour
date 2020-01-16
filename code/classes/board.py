import csv
import os
from sys import exit, argv

from colored import fg, stylize

from .car import Car


class RushHour():
    def __init__(self, board_path):
        '''
        Initializing variables.
        '''
        self.boardsize = int(argv[1][0] + argv[1][1]) if int(argv[1][0]) == 1 else int(argv[1][0]) 
        self.matrix = []
        self.cars = {}
        self.last_move = (None, 0)
        self.colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']
        self.load( board_path)
        self.steps = 0
        
    def load(self, board_path):
        '''
        Load cars from file and initialize matrix.
        '''            
        # try to open the given file and start reading
        try:
            with open(board_path, 'r') as in_file:
                reader = csv.DictReader(in_file)

                # loop over lines in file and adjust values for use in Car object
                for i, data in enumerate(reader):
                    # retrieve data from file
                    row = int(data['row'])
                    col = int(data['col'])
                    color = 'red_1' if data['car'] == 'X' else self.colors[i % len(self.colors)]

                    # create a list of cars on the board
                    self.cars[data['car']] = Car(data['car'], data['orientation'], row, col, color, int(data['length']))
        except FileNotFoundError:
            print('Invalid file')
            exit()

        # create gameboard
        for i in range(self.boardsize):
            self.matrix.append([0] * self.boardsize)

        # initialize gameboard, by placing cars
        for car in self.cars.values():
            try:
                self.matrix[car.row][car.col] = car

                # after first coördinate of car is placed, extend the car in it's direction
                if car.direction == 'H':
                    self.matrix[car.row][car.col + 1] = car
                    self.matrix[car.row][car.col + car.length - 1] = car
                else:
                    self.matrix[car.row - 1][car.col] = car
                    self.matrix[car.row - (car.length - 1)][car.col] = car
            except IndexError:
                print(f"{car.name} did not fit on board")
                exit()

    def printboard(self):
        '''
        Prints the current gameboard.
        '''
        # printing of the current gameboard
        for i, row in enumerate(self.matrix):
            for element in row:
                if not element:
                    print(stylize(u'\u25A0', fg('light_gray')), end=" ")
                else:
                    print(stylize(f'{element.name}', fg(element.color)), end=" ")

                # compensates the view of the board for 12x12 situation
                if len(self.cars) > 26 and (not element or len(element.name) < 2):
                    print(" ", end="")

            # draw an arrow at the exit
            if i == self.cars['X'].row:
                print('-->', end="")

            print()

    def move(self, car, distance):
        '''
        Attempts to move the car.
        '''
        # uses two for loops to delete and rebuild the car in the matrix, 
        # one loop would cause problems with small distances
        free_space = car.look_around(self)

        # checks if there is enough space to move the car
        if free_space['rear'] > distance or distance > free_space['front'] or distance == 0:
            return False

        if car.direction == 'H':
            for i in range(car.length):
                self.matrix[car.row][car.col + i] = 0

            for i in range(car.length):
                self.matrix[car.row][car.col + distance + i] = car
            
            car.position(car.row, car.col + distance)
        elif car.direction == 'V':
            for i in range(car.length):
                self.matrix[car.row - i][car.col] = 0

            for i in range(car.length):
                self.matrix[car.row - distance - i][car.col] = car
            
            car.position(car.row - distance, car.col)

        # remembers last move that was done on the board
        self.last_move = (car, distance)
        self.steps += 1
        return True
    
    def game_won(self):
        '''
        Returns True if the game is won, else false.
        '''
        # checks if the win conditions of the game are met
        if self.matrix[self.cars['X'].row][-1] == self.cars['X']:
            # os.system('cls')
            # self.printboard()
            print('Congratulations! The game was finished in:', self.steps, 'steps.')
            return True

        return False
