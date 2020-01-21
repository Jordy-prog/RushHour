boardstates = [('a', '1', 'A'), ('b', '2', 'B'), ('c', '3', 'C'), ('d', '4', 'D'), ('e', '5', 'E'), ('f', '6', 'A'), ('g', '7', 'B'), ('h', '8', 'A')]
boardstates_indexes = {}

i = 0
while i < len(boardstates):
    print(i)
    if boardstates[i][2] in boardstates_indexes:
        first = boardstates_indexes[boardstates[i][2]]
        last = i
        print(len(boardstates))
        del boardstates[first:last]

        for key in list(boardstates_indexes.keys())[first + 1:last]:
            del boardstates_indexes[key]
        print(len(boardstates))
        print(boardstates_indexes)
        i = first
    else:
        boardstates_indexes[boardstates[i][2]] = boardstates.index(boardstates[i])
        print(boardstates_indexes)

    i += 1

print(boardstates)