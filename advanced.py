import random
from code.algorithms.random import random_pure
from code.classes.car import Car
from code.classes.board import RushHour
from sys import argv
from colored import fg, stylize
import csv
import os

def advanced():
    # RushHour = board.RushHour(f'data/{argv[1]}')
    # make matrix
    # make cars dictionary
    # maybe write to csv
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AY', 'AZ']
    matrix = []
    cars = {}
    colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']
    boardsize = int(argv[1][0] + argv[1][1]) if int(argv[1][0]) == 1 else int(argv[1][0])

    for i in range(boardsize):
        matrix.append([0] * boardsize)

    space_to_occupy = (boardsize * boardsize) - ((boardsize * boardsize) // 4) - boardsize
    free_space = boardsize // 3

    # place red car
    row_x = (boardsize - 1) // 2
    col_x = random.randrange(0, boardsize - 2)
    cars['X'] = Car('X', 'H', row_x, col_x, 'red_1', 2)
    matrix[row_x][col_x] = cars['X']
    matrix[row_x][col_x + 1] = cars['X']  

    total_length = 0
    counter = 0 
    print('1')

    while total_length < space_to_occupy:
        possible_places = []
        percentage_length = random.random()
        length = (2 if percentage_length < 0.8 else 3)
        color = colors[counter % len(colors)]
        percentage_dir = random.random()
        direction = ('V' if percentage_dir < 0.7 else 'H')

        for row in range(boardsize):
            for col in range(boardsize):
                if direction == 'H':
                    occupied = False

                    for i in range(length):
                        try:
                            if matrix[row][col + i] or row == row_x or matrix[row].count(0) - length == 0:
                                occupied = True
                                break
                        except IndexError:
                            occupied = True
                            break
                elif direction == 'V':
                    occupied = False

                    for i in range(length):
                        try:
                            if row - i < 0 or matrix[row - i][col] or row - i == row_x or matrix[row - i].count(0) - 1 == 0:
                                occupied = True
                                break
                        except IndexError:
                            occupied = True
                            break

                if not occupied:
                    possible_places.append((row, col))
        print('2')
        if len(possible_places):
            position = random.choice(possible_places)
            name = names[counter]
            cars[name] = Car(name, direction, position[0], position[1], color, length)
            car = cars[name]
            matrix[car.row][car.col] = car

            # after first coördinate of car is placed, extend the car in it's direction
            if car.direction == 'H':
                matrix[car.row][car.col + 1] = car
                matrix[car.row][car.col + car.length - 1] = car
            else:
                matrix[car.row - 1][car.col] = car
                matrix[car.row - (car.length - 1)][car.col] = car

            total_length += length
            counter += 1
                            
    print(matrix)
    print(cars)

    for i, row in enumerate(matrix):
        for element in row:
            if not element:
                print(stylize(u'\u25A0', fg('light_gray')), end=" ")
            else:
                print(stylize(f'{element.name}', fg(element.color)), end=" ")

            # compensates the view of the board for 12x12 situation
            if len(cars) > 26 and (not element or len(element.name) < 2):
                print(" ", end="")

        # draw an arrow at the exit
        if i == cars['X'].row:
            print('-->', end="")

        print()

    car_list = []

    for car in cars.values():
        car_dict = {}
        car_dict['car'] = car.name
        car_dict['orientation'] = car.direction
        car_dict['row'] = car.row
        car_dict['col'] = car.col
        car_dict['length'] = car.length
        
        car_list.append(car_dict)

    with open(f'data/{argv[1]}', 'w', newline='') as file:
        fieldnames = ['car', 'orientation', 'row', 'col', 'length']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for car in car_list:
            writer.writerow(car)

    Rushhour = RushHour(f'data/{argv[1]}')

    for i in range(200):
        random_pure(Rushhour)

    car_list_new = []

    for car in Rushhour.cars.values():
        car_dict = {}
        car_dict['car'] = car.name
        car_dict['orientation'] = car.direction
        car_dict['row'] = car.row
        car_dict['col'] = car.col
        car_dict['length'] = car.length
        
        car_list_new.append(car_dict)

    with open(f'data/{argv[1]}', 'w', newline='') as file:
        fieldnames = ['car', 'orientation', 'row', 'col', 'length']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for car in car_list_new:
            writer.writerow(car)

    print()

    Rushhour.printboard()
    



if __name__ == '__main__':
    advanced()
    
