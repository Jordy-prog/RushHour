import copy
from sys import argv

from .random import random_constraint
from ..classes import board


def hillclimb(RushHour_initial):
    boardstates_initial = []

    # do one random run and save the moves that were done
    while not RushHour_initial.game_won():
        random_constraint(RushHour_initial)
        boardstates_initial.append(copy.deepcopy(RushHour_initial.matrix))

    RushHour_new = board.RushHour(f'data/{argv[1]}')
    



    # loop over random algoritme en laat algoritme 1 move returnen en sla die hier op in movelist
    # maak nieuw gameobject aan, loop over moves tot bepaalde toestand sla die op, loop verder tot nieuwe toestand, sla die ook op
    # start nu vanaf de nieuwe matrix en loop over random algoritme, en check na elke move of het bord in dezelfde toestand staat als de verst opgeslagen matrix door over matrix te loopen en te kijken of alles goed staat
    # als zelfde state gevonden is, pak de lijst met huidige moves en vergelijk hem met de lijst van moves tussen de twee opgeslagen states in.

    # selectieve eliminatie uit de movelist van een oplossing
    # random hoeft nu geen move meer te returnen want je slaat boardstates op