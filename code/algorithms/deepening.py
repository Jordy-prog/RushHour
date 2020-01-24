import copy
import re

def deepening(RushHour):
    """Implementation of the Iterative Deepening algorithm.
        
    Parameters:
        RushHour (object): The Rush Hour board object.

    Returns:
        True (boolean): The game has been won.
    """
    # Initialize depth and start algorithm
    depth = 0

    while True:
        # Initialize archive and stack with the initial Rush hour in them
        stack = [RushHour.steps]
        archive = {}
        archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)

        # Work through the stack and check all boards for solution
        while len(stack) > 0:
            # Take a parent from the top of the stack
            parent_moves = stack.pop()
            parent = copy.deepcopy(RushHour)

            for move in parent_moves:
                parent.move(parent.cars[move[0]], move[1])
    
            # Continue if this parent is still within the allowed depth
            if len(parent.steps) < depth:
                # Retrieve children from this parent and return if game is over
                children, winning_child = parent.get_children()
                
                if winning_child:
                    return True

                # Else append the unknown or better children to the stack
                for child in children:
                    if not child["matrix"] in archive or len(child["moves"]) < archive[child["matrix"]]:
                        archive[child["matrix"]] = len(child["moves"])
                        stack.append(child["moves"])

        depth += 1
        print(depth)