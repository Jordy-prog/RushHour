import copy
import re
import time
import random
from time import sleep
from .random import random_constraint

def dfs(RushHour):

    depth = []
    for i in range(50):
        run = copy.deepcopy(RushHour)
        while not run.game_won():
            move = random_constraint(run)
        depth.append(len(run.steps))
    depth = min(depth)
    print(depth)
    
    

    while True:
        print("a")
        # Initialize archive and queue with the initial Rush hour in them
        archive = {}
        archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)
        queue = [RushHour]

        # Work through the queue and check all boards for solution
        while len(queue):
            # Take a parent from the back of the queue
            parent = queue.pop()
            if len(parent.steps) % 10 == 0:
                print(len(parent.steps))
            children = []
            if len(parent.steps) < depth - 1:
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
                            depth = len(child.steps)

                        # Only add unknown boards to the archive and to the queue (optimal pruning)
                        board = re.sub(', ', '', str(child.matrix))
                        if board not in archive or len(child.steps) < archive[board]:
                            archive[board] = len(child.steps)
                            children.append(child)
                    
                    # Generate all children for moving this car backward
                    for distance in range(0, free_space['rear'], -1):
                        child = copy.deepcopy(parent)
                        child.move(child.cars[car.name], (distance - 1))

                        if child.game_won():
                            depth = len(child.steps)

                        board = re.sub(', ', '', str(child.matrix))
                        if board not in archive or len(child.steps) < archive[board]:
                            archive[board] = len(child.steps)
                            children.append(child)
                # random.shuffle(children)
                for i in range(len(children)):
                    queue.append(children[i])
 
        
        
            