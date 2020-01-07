import csv
from colored import fg, bg, stylize
from sys import exit, argv
from objects import Car

if len(argv) < 2:
    print('Usage: python matrix.py "filename"')
    exit()

class Rush():
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
            position = (self.boardsize - int(line[3].strip().strip('\"')), int(line[2].strip().strip('\"')) - 1)

            # assign the right color to the main car
            if line[0] == 'X':
                color = 'red_1'
            else:
                color = self.colors[i%len(self.colors)]

            # create a list of cars on the board
            self.cars[line[0]] = Car(line[0], line[1].strip(), position, color, int(line[4].strip()))

        # create gameboard
        for i in range(self.boardsize):
            self.matrix.append([0] * self.boardsize)

        # initialize gameboard, by placing cars
        for car in self.cars.values():
            try:
                self.matrix[car.start[0]][car.start[1]] = car

                # after first coördinate of car is placed, extend the car in it's direction
                if car.direction == 'H':
                    self.matrix[car.start[0]][car.start[1] + 1] = car
                    self.matrix[car.start[0]][car.start[1] + car.length - 1] = car
                else:
                    self.matrix[car.start[0] - 1][car.start[1]] = car
                    self.matrix[car.start[0] - (car.length - 1)][car.start[1]] = car
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

            # draw an arrow at the exit
            if i == self.cars['X'].start[0]:
                print('-->', end="")

            print()

def main():
    rush = Rush()
    rush.printboard()


if __name__ == '__main__':
    main()





