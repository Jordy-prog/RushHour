import os
from time import sleep

def manual(RushHour):
    steps = 0

    while not rush.game_won(steps):
        os.system('cls')
        rush.printboard()
        print('Moves:', steps)
        car_to_move = input('Which car do you want to move? ').upper()

        if not car_to_move.upper() in rush.cars.keys():
            print('Invalid car!')
            sleep(1)
            continue

        try:
            distance = int(input('How far? '))
        except ValueError:
            print('Invalid distance!')
            sleep(1)
            continue

        if not rush.move(rush.cars[car_to_move], distance):
            print('Invalid move!')
            sleep(1)
        else:
            steps += 1