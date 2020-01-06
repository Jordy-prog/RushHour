import numpy as np
import csv
from colored import fg, bg, stylize
from sys import exit

boardsize = 9
matrix = []
cars = []
colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']

class Car():
    def __init__(self, name, direction, position, color, length):
        self.name = name
        self.color = color
        self.length = length
        self.direction = direction
        self.start = position

        if self.start[1] >= boardsize or self.start[0] >= boardsize:
            print(f"{self.name} did not fit on board")
            exit()

    def __str__(self):
        return f"{self.name}"

with open('./gameboards/Rushhour9x9_5.csv') as file:
    next(file)
    text = csv.reader(file)
    for i, line in enumerate(text):
        position = (boardsize - int(line[3].strip().strip('\"')), int(line[2].strip().strip('\"')) - 1)

        if line[0] == 'X':
            color = 'red_1'
        else:
            color = colors[i%len(colors)]

        cars.append(Car(line[0], line[1].strip(), position, color, int(line[4].strip())))

for i in range(boardsize):
    matrix.append([0] * boardsize)

for car in cars:
    matrix[car.start[0]][car.start[1]] = car

    if car.direction == 'H':
        print('hoi')
        try:
            matrix[car.start[0]][car.start[1] + 1] = car
            matrix[car.start[0]][car.start[1] + car.length - 1] = car
        except IndexError:
            print(f'{car.name} does not fit on board')
            exit()
    
    else:
        try:
            matrix[car.start[0] - 1][car.start[1]] = car
            matrix[car.start[0] - (car.length - 1)][car.start[1]] = car
        except IndexError:
            print(f'{car.name} does not fit on board')
            exit()

for row in matrix:
    for element in row:
        if not element:
            print(stylize(u"\u25A0", fg('light_gray')), '', end="")
        else:
            print(stylize(u"\u25A0", fg(element.color)), '', end="")

    print()

