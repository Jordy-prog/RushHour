import copy
import re
import time
import random
from time import sleep
from .random import random_constraint

def dfs(RushHour):

    # depth = []
    # for i in range(100):
    #     run = copy.deepcopy(RushHour)
    #     while not run.game_won():
    #         move = random_constraint(run)
    #     depth.append(len(run.steps))
    # depth = min(depth)
    # print(depth)
    # depth = 10
    # Initialize archive and queue with the initial Rush hour in them
   
    #
    initial_depth = 23
    while True:
        archive = {}
        archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)
        queue = [RushHour.steps]
        depth = initial_depth
        print(depth)

        # Work through the queue and check all boards for solution
        while len(queue):
            # Take a parent from the back of the queue
            parent_moves = queue.pop()
            parent = copy.deepcopy(RushHour)
            for move in parent_moves:
                parent.move(parent.cars[move[0]], move[1])

            if len(parent.steps) < depth - 1:
                # Loop over the parent's cars to generate its children
                for car in parent.cars.values():
                    # Determine free space in front and behind the car
                    free_space = car.look_around(parent)

                    # Generate children for moving this car forward
                    for distance in range(free_space['front']):
                        # Create a copy for the child and move the car
                        parent.move(car, distance + 1)
                        
                        # Return True if this child results in a win
                        if parent.game_won():
                            depth = len(parent.steps)
                        last_move = parent.steps.pop()

                        # Only add unknown boards to the archive and to the queue (optimal pruning)
                        board = re.sub(', ', '', str(parent.matrix))
                        if board not in archive or len(parent.steps) < archive[board]:
                            archive[board] = len(parent.steps)
                            move_list = parent_moves + [last_move]
                            queue.append(move_list)

                        # Undo move to bring parent back to original state
                        parent.move(car, - (distance + 1))
                        parent.steps.pop()
                    
                    # Generate all children for moving this car backward
                    for distance in range(0, free_space['rear'], -1):
                        parent.move(car, (distance - 1))

                        if parent.game_won():
                            depth = len(parent.steps)
                        last_move = parent.steps.pop()

                        board = re.sub(', ', '', str(parent.matrix))
                        if board not in archive or len(parent.steps) < archive[board]:
                            archive[board] = len(parent.steps)
                            move_list = parent_moves + [last_move]
                            queue.append(move_list)

                        parent.move(car, - (distance - 1))
                        parent.steps.pop()
        if depth < initial_depth:
            print(depth)
            return
        initial_depth += 10
 
        
        
            