from objects import Car
import csv
import random

boardsize = 9
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

# RANDOM
car = random.choice(list(cars.values()))
# if car.blockfront:
    # Rush.move(car)
# elif car.blockback:
    # Rush.move(car)

# OBSTACLE CHAIN
leader = cars['X']
if leader.frontdistance > 0:
    Rush.move(leader)
else:
    obstacle = Matrix(leader.position + leader.length) # should be a car object
    while not Rush.move(obstacle):
        obstaclefront = Matrix(obstacle.position + obstacle.length)
        obstacleback = Matrix(obstacle.position + obstacle.length)



