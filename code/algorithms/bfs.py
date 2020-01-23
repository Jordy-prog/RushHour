import copy
import re
import time


def bfs(RushHour):
    # Initialize archive and queue with the initial Rush hour in them
    archive = set(re.sub(', ', '', str(RushHour.matrix)))
    queue = [RushHour.steps]

    # Work through the queue and check all boards for solution
    current_depth = 0
    while len(queue):
        # Take move list for parent from the front of the queue and execute moves
        parent_moves = queue.pop(0)
        parent = copy.deepcopy(RushHour)
        for move in parent_moves:
            parent.move(parent.cars[move[0]], move[1])

        children, winning_child = parent.get_children()
        
        if winning_child:
            return True

        for child in children:
            if not child["matrix"] in archive:
                archive.add(child["matrix"])
                queue.append(child["moves"])

        # If the algorithm goes a layer deeper into the tree, let the user know
        if len(parent.steps) > current_depth:
            current_depth += 1 
            print(current_depth)
            
        
        
            