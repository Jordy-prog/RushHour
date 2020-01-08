import csv
import os
from colored import fg, bg, stylize
from sys import exit, argv
from objects import Car
from algorithms import random_move
from time import sleep

if len(argv) < 2:
    print('Usage: python matrix.py "filename"')
    exit()

class RushHour():
    def __init__(self):
        '''
        Initializing variables.
        '''
        self.boardsize = int(argv[1][8])
        self.matrix = []
        self.cars = {}
        self.colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']
        self.load()

    def load(self):
        '''
        Load cars from file and initialize matrix.
        '''
        # read cars from file
        try:
            file = open(f'./gameboards/{argv[1]}')
        except FileNotFoundError:
            print('Invalid file')
            exit()
            
        # skip first line, and read rest of file
        next(file)
        text = csv.reader(file)

        # loop over lines in file and adjust values for use in Car object
        for i, line in enumerate(text):
            row = self.boardsize - int(line[3].strip().strip('\"'))
            col = int(line[2].strip().strip('\"')) - 1

            # assign the right color to the main car
            if line[0] == 'X':
                color = 'red_1'
            else:
                color = self.colors[i%len(self.colors)]

            # create a list of cars on the board
            self.cars[line[0]] = Car(line[0], line[1].strip(), row, col, color, int(line[4].strip()))

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
        
        file.close()

    def printboard(self):
        '''
        Prints the current gameboard.
        '''
        # printing of the current gameboard
        for i, row in enumerate(self.matrix):
            for element in row:
                if not element:
                    print(stylize(u'\u25A0', fg('light_gray')), '', end="")
                else:
                    print(stylize(f'{element.name}', fg(element.color)), '', end="")

            # draw an arrow at the exit
            if i == self.cars['X'].row:
                print('-->', end="")

            print()

    def move(self, car, distance):
        step = -1 if distance < 0 else 1

        if car.direction == 'H':
            # forloop check if car can move, for manual purposes only!
            for i in range(step, distance + step, step):
                try:
                    if car.col + i < 0 or step == -1 and self.matrix[car.row][car.col + i] or step == 1 and self.matrix[car.row][car.col + i + (car.length - 1)]:
                        return False
                except IndexError:
                    return False

            for i in range(car.length):
                self.matrix[car.row][car.col + i] = 0

            for i in range(car.length):
                self.matrix[car.row][car.col + distance + i] = car
            
            car.position(car.row, car.col + distance)
        elif car.direction == 'V':
            # forloop check if car can move, for manual purposes only!
            for i in range(step, distance + step, step):
                try:
                    if car.row - (car.length - 1) - i < 0 or step == -1 and self.matrix[car.row - i][car.col] or step == 1 and self.matrix[car.row - i - (car.length - 1)][car.col]:
                        return False
                except IndexError:
                    return False

            for i in range(car.length):
                self.matrix[car.row - i][car.col] = 0

            for i in range(car.length):
                self.matrix[car.row - distance - i][car.col] = car
            
            car.position(car.row - distance, car.col)

        return True
    
    def game_won(self):
        if self.matrix[self.cars['X'].row][-1] == self.cars['X']:
            print('Congratulations!')
            return True

        return False

def main():
    manual = False
    rush = RushHour()
    rush.printboard()

    

    if manual:
        while not rush.game_won():
            car_to_move = input('Which car do you want to move? ').upper()

            if not car_to_move.upper() in rush.cars.keys():
                print('Unable to move that car in that direction!')
                sleep(1)
                continue

            try:
                distance = int(input('How far? '))
            except ValueError:
                print('Invalid distance')
                sleep(1)
                continue

            if not rush.move(rush.cars[car_to_move], distance):
                print('Too bad sucker')
                sleep(1)
            sleep(2)
            os.system('cls')
            rush.printboard()
    else:
        while not rush.game_won():
            random_move(rush)
            os.system('cls')
            rush.printboard()

if __name__ == '__main__':
    main()





