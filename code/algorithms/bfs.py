import copy
import re
import time


def bfs(RushHour):
    # Initialize archive and queue with the initial Rush hour in them
    archive = set()
    queue = [RushHour.steps]

    # Work through the queue and check all boards for solution
    current_depth = 0
    i = 0
    while len(queue):
        # Take move list for parent from the front of the queue and execute moves
        # i += 1
        parent_moves = queue.pop(0)
        parent = copy.deepcopy(RushHour)
        for move in parent_moves:
            parent.move(parent.cars[move[0]], move[1])

        
        children, winning_child = parent.get_children()
        
        if winning_child:
            return True

        for child in children:
            if child["matrix"] not in archive:
                archive.add(child["matrix"])
                queue.append(child["moves"])

        # # # print(len(archive))

        # # Loop over the parent's cars to generate its children
        # for car in parent.cars.values():
        #     # Determine free space in front and behind the car
        #     free_space = car.look_around(parent)
            
        #     # Generate children for moving this car forward
        #     for distance in range(free_space['front']):
        #         # Move the car on the parent
        #         parent.move(car, distance + 1)
                
        #         # Return True if this move results in a win, else pop the last move
        #         if parent.game_won():
        #             return True
        #         last_move = parent.steps.pop() 

        #         # Only add unknown boards to the archive and to the queue (optimal pruning)
        #         board = re.sub(', ', '', str(parent.matrix))
        #         if board not in archive:
        #             archive.add(board)

        #             # Add the last move to the move_list that creates this child and add to queue
        #             move_list = parent_moves + [last_move]
        #             queue.append(move_list)

        #         # Undo move to bring parent back to original state
        #         parent.move(car, - (distance + 1))
        #         parent.steps.pop()
            
        #     # Generate all children for moving this car backward
        #     for distance in range(0, free_space['rear'], -1):
        #         parent.move(car, (distance - 1))

        #         if parent.game_won():
        #             return True
        #         last_move = parent.steps.pop()

        #         board = re.sub(', ', '', str(parent.matrix))
        #         if board not in archive:
        #             archive.add(board)
        #             move_list = parent_moves + [last_move]
        #             queue.append(move_list)

        #         parent.move(car, - (distance - 1))
        #         parent.steps.pop()


        # If the algorithm goes a layer deeper into the tree, let the user know
        if len(parent.steps) > current_depth:
            current_depth += 1 
            print(current_depth, len(archive))
            
        
        
            