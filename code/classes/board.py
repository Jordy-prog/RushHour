import copy
import csv
import os
import re
from sys import argv

from colored import fg, stylize

from .car import Car


class RushHour():
    """A class which stores information of the board object.

    The contained methods are as follows:
        __init__: Intialize board variables.
        load: Load cars and initialize the matrix.
        printboard: Prints the current game board.
        move: Attempts to move the car.
        get_children: Determines which boards can be derived from the current board.
        game_won: Checks if the current game has been won.
    """

    def __init__(self, board_path):
        """__init__ function to initialize variables.
        
        Parameters:
            board_path (string): File path to the desired board.
        """
        self.boardsize = int(argv[1][0] + argv[1][1]) if int(argv[1][0]) == 1 else int(argv[1][0]) 
        self.matrix = []
        self.cars = {}
        self.colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']
        self.load(board_path)
        self.steps = []
        
    def load(self, board_path):
        """Load cars from file and initialize the matrix.
        
        Parameters:
            board_path (string): File path to the desired board.
        """      
        # Try to open the given file and start reading
        try:
            with open(board_path, 'r') as in_file:
                reader = csv.DictReader(in_file)

                # Loop over lines in file and adjust values for use in Car object
                for i, data in enumerate(reader):
                    # Retrieve data from file
                    row = int(data['row'])
                    col = int(data['col'])
                    color = 'red_1' if data['car'] == 'X' else self.colors[i % len(self.colors)]

                    # Create a list of cars on the board
                    self.cars[data['car']] = Car(data['car'], data['orientation'], row, col, color, int(data['length']))
        except FileNotFoundError:
            print(board_path)
            print('Invalid file')
            exit()

        # Create gameboard
        for i in range(self.boardsize):
            self.matrix.append([0] * self.boardsize)

        # Initialize gameboard, by placing cars
        for car in self.cars.values():
            try:
                self.matrix[car.row][car.col] = car

                # After first coördinate of car is placed, extend the car in it's orientation
                if car.orientation == 'H':
                    self.matrix[car.row][car.col + 1] = car
                    self.matrix[car.row][car.col + car.length - 1] = car
                else:
                    self.matrix[car.row - 1][car.col] = car
                    self.matrix[car.row - (car.length - 1)][car.col] = car
            except IndexError:
                print(f"{car.name} did not fit on board")
                exit()

    def printboard(self):
        """Prints the current gameboard."""
        # Printing of the current gameboard
        for i, row in enumerate(self.matrix):
            for element in row:
                if not element:
                    print(stylize(u'\u25A0', fg('light_gray')), end=" ")
                else:
                    print(stylize(f'{element.name}', fg(element.color)), end=" ")

                # Compensates the view of the board for 12x12 situation
                if len(self.cars) > 26 and (not element or len(element.name) < 2):
                    print(" ", end="")

            # Draw an arrow at the exit
            if i == self.cars['X'].row:
                print('-->', end="")

            print()

    def move(self, car, distance):
        """Attempts to move the car.
        Uses two for loops to delete and rebuild the car in the matrix.
        
        Parameters:
            car (object): The car object to move.
            distance (int): The distance the car should move.
        
        Returns:
            False (boolean): The car isn't able to move.
            True (boolean): The car was successfully moved
        """
        free_space = car.look_around(self)

        # Checks if there is enough space to move the car
        if free_space['rear'] > distance or distance > free_space['front'] or distance == 0:
            return False

        # Move car
        if car.orientation == 'H':
            for i in range(car.length):
                self.matrix[car.row][car.col + i] = 0

            for i in range(car.length):
                self.matrix[car.row][car.col + distance + i] = car
            
            car.set_position(car.row, car.col + distance)
        elif car.orientation == 'V':
            for i in range(car.length):
                self.matrix[car.row - i][car.col] = 0

            for i in range(car.length):
                self.matrix[car.row - distance - i][car.col] = car
            
            car.set_position(car.row - distance, car.col)

        # Remembers last move that was done on the board
        self.steps.append((car.name, distance))
        return True
    
    def get_children(self):
        """Determines which boards can be derived from the current board.
        
        Returns:
            children (list): List of dictionaries containing the matrix and move list of a child.
            winning_child (list): move list of the winning child if present
        """
        children = []
        winning_child = []
        
        # Loop over the cars to generate the children
        for car in self.cars.values():
            # Determine free space in front and behind the car
            free_space = car.look_around(self)

            # Generate children for moving this car
            for free_space in range(free_space["rear"], free_space["front"]):
                # Modify the distance for positive movement and move car
                distance = free_space if free_space < 0 else free_space + 1
                self.move(car, distance)
                
                # Register child if it results in a win
                if self.game_won():
                    winning_child = copy.deepcopy(self.steps)
                
                # Create the dictionary with data of this child and add to list
                move = [self.steps.pop()]
                matrix = re.sub(', ', '', str(self.matrix))
                children.append({"moves": self.steps + move, "matrix": matrix})

                # Undo move to bring parent back to original state
                self.move(car, - distance)
                self.steps.pop()

        return children, winning_child

    def game_won(self):
        """Function to check if the current game has been won.

        Returns:
            True (boolean): The game has been won.
            False (boolean): The game is not won yet.
        """
        # Checks if the win conditions of the game are met
        if self.matrix[self.cars['X'].row][-1] == self.cars['X']:
            self.write_csv()
            print('Congratulations! The game was finished in:', len(self.steps), 'steps.')
            return True

        return False

    def write_csv(self):
        """Writes the moves that were done to a csv file."""
        step_list = []

        # Create dictionary of steps for writing
        for step in self.steps:
            step_dict = {}
            step_dict['car'] = step[0]
            step_dict['distance'] = step[1]

            step_list.append(step_dict)

        # Open a file for writing, and write the csv file
        with open(f'output/last_solution.csv', 'w', newline='') as file:
            fieldnames = ['car', 'distance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for step in step_list:
                writer.writerow(step)
