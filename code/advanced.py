from .algorithms import random
from .classes import board, car

def advanced():
    RushHour = board.RushHour(f'data/{argv[1]}')
    # make matrix
    # make cars dictionary
    # maybe write to csv
    names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    matrix = []
    cars = {}
    colors = ['blue_1', 'yellow_1', 'green_1', 'dark_green', 'deep_pink_1a', 'dark_orange']
    boardsize = int(argv[1][0] + argv[1][1]) if int(argv[1][0]) == 1 else int(argv[1][0])

    for i in range(boardsize):
        matrix.append([0] * boardsize)

    free_spaces = (boardsize * boardsize) // 3

    length = random.randrange(2,4)
    row_x = boardsize - 1 // 2
    col_x = random.randrange(0, boardsize - 1)
    color = random.choice(colors)
    direction = random.choice(['V', 'H'])

    while total_length < free_spaces:
        possible_places = []
        length = random.randrange(2,4)
        color = random.choice(colors)
        direction = random.choice(['V', 'H'])

        for row in range(boardsize):
            for col in range(boardsize):
                if direction == 'H':
                    occupied = False

                    for i in range(length):
                        try:
                            if matrix[row][col + i]:
                                occupied = True
                                break
                        except IndexError:
                            break

                    possible_places.append((row, col))
                else:
                    occupied = False

                    for i in range(length):
                        try:
                            if matrix[row + i][col]:
                                occupied = True
                                break
                        except IndexError:
                            break

                    possible_places.append((row, col))
                            

    cars['X'] = Car('X', 'H', row_x, col_x, 'red_1', 2)
