import copy
import os
import random
from sys import argv
from time import sleep

from .random import random_constraint
from ..classes import board


def hillclimb(RushHour_initial, slices, improvements):
    boardstates = []

    # do one random run and save the moves that were done
    while not RushHour_initial.game_won():
        random_constraint(RushHour_initial)
        boardstates.append(copy.deepcopy(RushHour_initial.matrix))

    print(len(boardstates))

    # cut that shit
    for i, boardstate in enumerate(boardstates):
        indexes = list(j for j, check in enumerate(boardstates[i + 1:], 1) if str(check) == str(boardstate))

        if indexes:
            first = i
            last = i + indexes[-1]
            del boardstates[first:last]

    print(len(boardstates))
    slice_times = 0

    while slice_times < slices:
        slice_times += 1
        print('slice:', slice_times)
        first_slice = random.randrange(0, len(boardstates)//2)
        last_slice = random.randrange(len(boardstates)//2, len(boardstates))
        boardstates_initial = copy.deepcopy(boardstates[first_slice:last_slice])
        RushHour_template = board.RushHour(f'data/{argv[1]}')
        RushHour_template.matrix = copy.deepcopy(boardstates_initial[0])

        for row in RushHour_template.matrix:
            for car in row:
                if car:
                    RushHour_template.cars[car.name].row = car.row
                    RushHour_template.cars[car.name].col = car.col

        improvement_times = 0

        while improvement_times < improvements:
            improvement_times += 1
            RushHour_new = copy.deepcopy(RushHour_template)
            boardstates_new = [copy.deepcopy(RushHour_new.matrix)]

            while not str(boardstates_new[-1]) == str(boardstates_initial[-1]) and len(boardstates_new) < len(boardstates_initial):
                random_constraint(RushHour_new)
                boardstates_new.append(copy.deepcopy(RushHour_new.matrix))

            if len(boardstates_new) < len(boardstates_initial):
                del boardstates[first_slice:last_slice]
                print('Improved')

                for i, boardstate in enumerate(boardstates_new):
                    boardstates.insert(first_slice + i, boardstate)

                break
    
    print(len(boardstates))
    # loop over random algoritme en laat algoritme 1 move returnen en sla die hier op in movelist
    # maak nieuw gameobject aan, loop over moves tot bepaalde toestand sla die op, loop verder tot nieuwe toestand, sla die ook op
    # start nu vanaf de nieuwe matrix en loop over random algoritme, en check na elke move of het bord in dezelfde toestand staat als de verst opgeslagen matrix door over matrix te loopen en te kijken of alles goed staat
    # als zelfde state gevonden is, pak de lijst met huidige moves en vergelijk hem met de lijst van moves tussen de twee opgeslagen states in.

    # selectieve eliminatie uit de movelist van een oplossing
    # random hoeft nu geen move meer te returnen want je slaat boardstates op
