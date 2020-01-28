import csv

def execute_move_list(board, move_list):
    """Exectues the move list.

    Parameters:
        board (object): The game board object.
        move_list (list): A list containing all moves.

    Returns:
        board (object): The finished game board object.
    """
    for move in move_list:
        board.move(board.cars[move[0]], move[1])

    return board

def elimination(movelist):
    """Searches for double boardstates in a movelist, 
    and eliminates everything in between.

    Parameters:
        movelist (list): A list of moves.

    Returns:
        len(movelist) (integer): The length of the final movelist.
    """
    move_indexes = {}
    i = 0
    
    while i < len(movelist):
        if movelist[i]['matrix'] in move_indexes:
            first = move_indexes[movelist[i]['matrix']]
            last = i
            del movelist[first:last]
            i = first

            for key in list(move_indexes.keys())[first + 1:]:
                del move_indexes[key]
        else:
            move_indexes[movelist[i]['matrix']] = movelist.index(movelist[i])
            
        i += 1
    
    return len(movelist)

def write_csv(steps):
    """Writes the moves that were done to a csv file.
    
    Parameters:
        steps (list): list of moves to be written to csv file
    """
    step_list = []

    # Create dictionary of steps for writing
    for step in steps:
        step_dict = {}
        step_dict['car'] = step[0]
        step_dict['distance'] = step[1]

        step_list.append(step_dict)

    # Open a file for writing, and write the csv file
    with open(f'results/last_solution.csv', 'w', newline='') as file:
        fieldnames = ['car', 'distance']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for step in step_list:
            writer.writerow(step)