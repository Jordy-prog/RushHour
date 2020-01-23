import os
from time import sleep


def manual(RushHour):
    """Implements a manual gameplay variation of the Rushhour game.

    Parameters:
        RushHour (object): The Rush Hour board object.
    """
    # Plays the game until it is won
    while not RushHour.game_won():
        # Clears terminal and prints useful information
        os.system('cls')
        RushHour.printboard()
        print('Number of moves:', len(RushHour.steps))
        print('Moves:', RushHour.steps)
        car_to_move = input('Which car do you want to move? ').upper()

        # Checks if car exists
        if not car_to_move.upper() in RushHour.cars.keys():
            print('Invalid car!')
            sleep(1)
            continue
        
        car = RushHour.cars[car_to_move]

        # Makes sure someone chooses a valid distance
        try:
            distance = int(input('How far? '))
            free_space = car.look_around(RushHour)

            # Checks if there is enough space to move the car
            if free_space['rear'] > distance or distance > free_space['front'] or distance == 0:
                print('Invalid distance!')
                sleep(1)
                continue

        except ValueError:
            print('Invalid distance!')
            sleep(1)
            continue

        # Moves the car
        RushHour.move(car, distance)