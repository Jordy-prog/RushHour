import os
from time import sleep

def manual(RushHour):
    steps = 0

    while not RushHour.game_won(steps):
        os.system('cls')
        RushHour.printboard()
        print('Moves:', steps)
        car_to_move = input('Which car do you want to move? ').upper()

        if not car_to_move.upper() in RushHour.cars.keys():
            print('Invalid car!')
            sleep(1)
            continue

        try:
            distance = int(input('How far? '))
        except ValueError:
            print('Invalid distance!')
            sleep(1)
            continue

        if not RushHour.move(RushHour.cars[car_to_move], distance):
            print('Invalid move!')
            sleep(1)
        else:
            steps += 1