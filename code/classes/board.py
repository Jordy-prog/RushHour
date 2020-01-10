import csv
from colored import fg, stylize
from sys import exit, argv
from .car import Car


class RushHour():
    def __init__(self, board_path):
        '''
        Initializing variables.
        '''
        # FIX ERROR CHECK THAT CHECKS IF FILE IS CORRECT FIRST
        self.boardsize = int(argv[1][0] + argv[1][1]) if int(argv[1][0]) == 1 else int(argv[1][0]) 
        self.matrix = []
        self.cars = {}
        self.last_move = (None, 0)
        self.colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']
        self.load( board_path)
        

    def load(self, board_path):
        '''
        Load cars from file and initialize matrix.
        '''            
        # try to open the given file and start reading
        try:
            with open(board_path, 'r') as in_file:
                reader = csv.DictReader(in_file)

                # loop over lines in file and adjust values for use in Car object
                for i, car in enumerate(reader):
                    row = int(car['row'])
                    col = int(car['col'])

                    # assign the right color to the main car
                    if car['car'] == 'X':
                        color = 'red_1'
                    else:
                        color = self.colors[i%len(self.colors)]

                    # create a list of cars on the board
                    self.cars[car['car']] = Car(car['car'], car['orientation'], row, col, color, int(car['length']))
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
                    print(stylize(u'\u25A0', fg('light_gray')), '', end="")
                else:
                    print(stylize(f'{element.name}', fg(element.color)), '', end="")

                if len(self.cars) > 26 and ((element and len(element.name) < 2) or not element):
                    print(" ", end="")

            # draw an arrow at the exit
            if i == self.cars['X'].row:
                print('-->', end="")

            print()

    def move(self, car, distance):
        if self.last_move == car:
            return False
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

        self.last_move = (car, distance)
        return True
    
    def game_won(self):
        if self.matrix[self.cars['X'].row][-1] == self.cars['X']:
            print('Congratulations!')
            return True

        return False