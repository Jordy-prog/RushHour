def execute_move_list(board, move_list):
    for move in move_list:
        board.move(board.cars[move[0]], move[1])

    return board

def elimination(movelist):
    move_indexes = {}
    i = 0
    
    # Selective elimination of double boardstates
    while i < len(movelist):
        # If boardstate is found multiple times in moveset, delete everything in between
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