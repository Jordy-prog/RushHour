import copy
import re


def bfs(RushHour):
    """An implementation of the Bread First algorithm.
        
    Parameters:
        RushHour (object): The Rush Hour board object.

    Returns:
        True (boolean): The game has been won.
    """
    # Initialize archive and queue with the initial Rush hour in them
    archive = set()
    archive.add(re.sub(', ', '', str(RushHour.matrix)))
    queue = [RushHour.steps]

    # Work through the queue and check all boards for solution
    current_depth = 0

    while len(queue):
        # Take move list for parent from the front of the queue and execute moves
        parent_moves = queue.pop(0)
        parent = copy.deepcopy(RushHour)

        for move in parent_moves:
            parent.move(parent.cars[move[0]], move[1])

        # Retrieve children from this parent and return if game is over
        children, winning_child = parent.get_children()
        
        if winning_child:
            return True

        # Else append the unknown children to the queue
        for child in children:
            if not child["matrix"] in archive:
                archive.add(child["matrix"])
                queue.append(child["moves"])

        # If the algorithm goes a layer deeper into the tree, let the user know
        if len(parent.steps) > current_depth:
            current_depth += 1
            print(current_depth)