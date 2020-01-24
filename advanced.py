import csv
import os
import random
from sys import argv

from code.algorithms.random import random_pure
from code.classes.board import RushHour
from code.classes.car import Car


def advanced():
    """This function generates random solved boards, and shuffles them with a random algorithm.
    The board is saved in a csv file and takes 1 argument (the filename) as input.

    Returns:
        False (boolean): ...
    """
    # Check if user writes csv filename
    if not argv[1][-4:] == '.csv':
        print('Invalid filename')
        return

    # Checks if file exists as a failsave
    if os.path.isfile(f'data/{argv[1]}'):
        while True:
            confirm = input('That file already exists, do you want to overwrite it?' )

            if confirm in ['yes', 'y']:
                break
            elif confirm in ['no', 'n']:
                return

    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AY', 'AZ']
    matrix = []
    cars = {}
    colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']
    boardsize = int(argv[1][0] + argv[1][1]) if int(argv[1][0]) == 1 else int(argv[1][0])

    # Setup an empty board
    for i in range(boardsize):
        matrix.append([0] * boardsize)

    # Setup variables that determine how many cars should be placed
    space_to_occupy = (boardsize * boardsize) - ((boardsize * boardsize) // 4) - boardsize

    # Place red car
    row_x = (boardsize - 1) // 2
    col_x = random.randrange(0, boardsize - 2)
    cars['X'] = Car('X', 'H', row_x, col_x, 'red_1', 2)
    matrix[row_x][col_x] = cars['X']
    matrix[row_x][col_x + 1] = cars['X']  

    total_length = 0
    counter = 0 

    # Generates cars and places them on the board
    while total_length < space_to_occupy:
        # Determine, the length, color and orientation of the car
        possible_places = []
        percentage_length = random.random()
        length = (2 if percentage_length < 0.8 else 3)
        color = colors[counter % len(colors)]
        percentage_dir = random.random()
        orientation = ('V' if percentage_dir < 0.7 else 'H')

        # Check where a car can possibly stand on the board and add that to a list
        for row in range(boardsize):
            for col in range(boardsize):
                if orientation == 'H':
                    occupied = False

                    # Make sure a car can stand on a place, and make sure it can't stand in the row of the red car
                    for i in range(length):
                        try:
                            if matrix[row][col + i] or row == row_x or matrix[row].count(0) - length == 0:
                                occupied = True
                                break
                        except IndexError:
                            occupied = True
                            break
                elif orientation == 'V':
                    occupied = False

                    # Make sure a car can stand on a place, and make sure it can't stand in the row of the red car
                    for i in range(length):
                        try:
                            if row - i < 0 or matrix[row - i][col] or row - i == row_x or matrix[row - i].count(0) - 1 == 0:
                                occupied = True
                                break
                        except IndexError:
                            occupied = True
                            break

                # Append possible place to a list
                if not occupied:
                    possible_places.append((row, col))

        # If there are places where the car can stand, pick one randomly and place the car
        if len(possible_places):
            position = random.choice(possible_places)
            name = names[counter]
            cars[name] = Car(name, orientation, position[0], position[1], color, length)
            car = cars[name]
            matrix[car.row][car.col] = car

            # After first coördinate of car is placed, extend the car in it's orientation
            if car.orientation == 'H':
                matrix[car.row][car.col + 1] = car
                matrix[car.row][car.col + car.length - 1] = car
            else:
                matrix[car.row - 1][car.col] = car
                matrix[car.row - (car.length - 1)][car.col] = car

            total_length += length
            counter += 1

    # Create solved csv_file for use of random algorithm
    write_csv(cars.values())
    Rushhour = RushHour(f'data/{argv[1]}')

    # Shuffle the board
    for i in range(1000):
        random_pure(Rushhour)

    # Overwrite previous csv file with a shuffled one
    write_csv(Rushhour.cars.values())
    
def write_csv(cars):
    """Creates a csv_file of the current board.

    Parameters:
        cars (dictionary values): A list of car objects.
    """
    car_list = []

    # Loop over cars and retrieve useful values
    for car in cars:
        car_dict = {}
        car_dict['car'] = car.name
        car_dict['orientation'] = car.orientation
        car_dict['row'] = car.row
        car_dict['col'] = car.col
        car_dict['length'] = car.length
        
        car_list.append(car_dict)

    # Open a file for writing, and write the csv file
    with open(f'data/{argv[1]}', 'w', newline='') as file:
        fieldnames = ['car', 'orientation', 'row', 'col', 'length']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for car in car_list:
            writer.writerow(car)


if __name__ == '__main__':
    advanced()
    
