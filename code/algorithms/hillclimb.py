import ..modes

def hillclimb(RushHour):
    # do one random run and save the moves that were done
    algorithm = '2' # random_constraint
    to_print = 'no'
    modes.test(RushHour, algorithm, to_print)

    # Sla alle moves op van de eerste run
    # loop over alle moves heen en zet ze op een nieuw spelbord
    # sla de twee tussenstates op in aparte matrix
    # laad aparte matrix in en run opnieuw het random algoritme nu vanuit dit algoritme
    # Elke keer moet die move ook weer worden opgeslagen
    # vergelijk lengte van move lijsten

    # Is het niet beter om te checken of een auto kan bewegen in de manual ipv in move, want nu checkt ie dubbel voor andere algoritmes
    # while loop met steps uit modes halen en in algoritmes zelf pleuren