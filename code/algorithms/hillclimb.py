import ..modes

def hillclimb(RushHour):
    # do one random run and save the moves that were done
    algorithm = '2' # random_constraint
    to_print = 'no'
    modes.test(RushHour, algorithm, to_print)

    # loop over random algoritme en laat algoritme 1 move returnen en sla die hier op in movelist
    # maak nieuw gameobject aan, loop over moves tot bepaalde toestand sla die op, loop verder tot nieuwe toestand, sla die ook op
    # start nu vanaf de nieuwe matrix en loop over random algoritme, en check na elke move of het bord in dezelfde toestand staat als de verst opgeslagen matrix door over matrix te loopen en te kijken of alles goed staat
    # als zelfde state gevonden is, pak de lijst met huidige moves en vergelijk hem met de lijst van moves tussen de twee opgeslagen states in.

    # Sla alle moves op van de eerste run
    # loop over alle moves heen en zet ze op het nieuwe spelbord vanaf de start
    # sla de twee tussenstates op in aparte matrix
    # laad aparte matrix in en run opnieuw het random algoritme nu vanuit dit algoritme
    # Elke keer moet die move ook weer worden opgeslagen
    # vergelijk lengte van move lijsten

    # Is het niet beter om te checken of een auto kan bewegen in de manual ipv in move, want nu checkt ie dubbel voor andere algoritmes
    # while loop met steps uit modes halen en in algoritmes zelf pleuren