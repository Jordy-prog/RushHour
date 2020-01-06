import csv
from colored import fg, bg, stylize
from sys import exit
from objects import Car

# initializing variables
boardsize = 9
matrix = []
cars = {}
colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']

# read cars from file
with open('./gameboards/Rushhour9x9_5.csv') as file:
    # skip first line, and read rest of file
    next(file)
    text = csv.reader(file)

    # loop over lines in file and adjust values for use in Car object
    for i, line in enumerate(text):
        position = (boardsize - int(line[3].strip().strip('\"')), int(line[2].strip().strip('\"')) - 1)

        # assign the right color to the main car
        if line[0] == 'X':
            color = 'red_1'
        else:
            color = colors[i%len(colors)]

        # create a list of cars on the board
        cars[line[0]] = Car(line[0], line[1].strip(), position, color, int(line[4].strip()))

# create gameboard
for i in range(boardsize):
    matrix.append([0] * boardsize)

# initialize gameboard, by placing cars
for car in cars.values():
    try:
        matrix[car.start[0]][car.start[1]] = car

        # after first coördinate of car is placed, extend the car in it's direction
        if car.direction == 'H':
                matrix[car.start[0]][car.start[1] + 1] = car
                matrix[car.start[0]][car.start[1] + car.length - 1] = car
        else:
                matrix[car.start[0] - 1][car.start[1]] = car
                matrix[car.start[0] - (car.length - 1)][car.start[1]] = car
    except IndexError:
        print(f"{car.name} did not fit on board")
        exit()

# printing of the current gameboard
for i, row in enumerate(matrix):
    for element in row:
        if not element:
            print(stylize(u"\u25A0", fg('light_gray')), '', end="")
        else:
            print(stylize(u"\u25A0", fg(element.color)), '', end="")

    # draw an arrow at the exit
    if i == cars['X'].start[0]:
        print('-->', end="")

    print()

