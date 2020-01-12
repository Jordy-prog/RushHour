import os
from time import sleep


def manual(RushHour):
    '''
    Function that implements a manual gameplay of Rushhour.
    '''
    steps = 0

    # plays the game until it is won
    while not RushHour.game_won(steps):
        # clears terminal and prints useful information
        os.system('cls')
        RushHour.printboard()
        print('Moves:', steps)
        car_to_move = input('Which car do you want to move? ').upper()

        # checks if car exists
        if not car_to_move.upper() in RushHour.cars.keys():
            print('Invalid car!')
            sleep(1)
            continue

        # makes sure someone chooses a valid distance
        try:
            distance = int(input('How far? '))
        except ValueError:
            print('Invalid distance!')
            sleep(1)
            continue

        # tries to move the car
        if not RushHour.move(RushHour.cars[car_to_move], distance):
            print('Invalid move!')
            sleep(1)
        else:
            steps += 1