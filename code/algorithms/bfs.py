import copy
import re
import time

def bfs(RushHour):
    # Initialize archive and queue with the initial Rush hour in them
    archive = set()
    archive.add(re.sub(', ', '', str(RushHour.matrix)))
    queue = [RushHour]

    # Work through the queue and check all boards for solution
    current_depth = 0
    while len(queue):
        # Take a parent from the front of the queue
        parent = queue.pop(0)

        # Loop over the parent's cars to generate its children
        for car in parent.cars.values():
            # Determine free space in front and behind the car
            free_space = car.look_around(parent)

            # Generate children for moving this car forward
            for distance in range(free_space['front']):
                # Create a copy for the child and move the car
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], distance + 1)

                # Return True if this child results in a win
                if child.game_won():
                    return True

                # Only add unknown boards to the archive and to the queue (optimal pruning)
                board = re.sub(', ', '', str(child.matrix))
                if board not in archive:
                    archive.add(board)
                    queue.append(child)
            
            # Generate all children for moving this car backward
            for distance in range(0, free_space['rear'], -1):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], (distance - 1))

                if child.game_won():
                    return True

                board = re.sub(', ', '', str(child.matrix))
                if board not in archive:
                    archive.add(board)
                    queue.append(child)
                    
        # If the algorithm goes a layer deeper into the tree, let the user know
        if len(parent.steps) > current_depth:
            current_depth += 1 
            print(current_depth)
        
        
            