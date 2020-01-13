import .random

def hillclimb(RushHour):
    moves_first = []

    # do one random run and save the moves that were done
    while not RushHour.game_won(steps):
        moves_first.append(random.random_constraint(RushHour))



    # loop over random algoritme en laat algoritme 1 move returnen en sla die hier op in movelist
    # maak nieuw gameobject aan, loop over moves tot bepaalde toestand sla die op, loop verder tot nieuwe toestand, sla die ook op
    # start nu vanaf de nieuwe matrix en loop over random algoritme, en check na elke move of het bord in dezelfde toestand staat als de verst opgeslagen matrix door over matrix te loopen en te kijken of alles goed staat
    # als zelfde state gevonden is, pak de lijst met huidige moves en vergelijk hem met de lijst van moves tussen de twee opgeslagen states in.

    # selectieve eliminatie uit de movelist van een oplossing