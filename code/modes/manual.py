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
        
        car = RushHour.cars[car_to_move]

        # makes sure someone chooses a valid distance
        try:
            distance = int(input('How far? '))
            free_space = car.look_around(RushHour)

            # checks if there is enough space to move the car
            if free_space['rear'] > distance or distance > free_space['front'] or distance == 0:
                print('Invalid distance!')
                sleep(1)
                continue

        except ValueError:
            print('Invalid distance!')
            sleep(1)
            continue

        # moves the car
        RushHour.move(car, distance)
        steps += 1