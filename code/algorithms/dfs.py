import copy
import random
import re

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
        stack = [RushHour.steps]
        depth = initial_depth
        print(depth)

        # Work through the queue and check all boards for solution
        while len(stack):
            # Take a parent from the back of the queue
            parent_moves = stack.pop()
            parent = copy.deepcopy(RushHour)
            for move in parent_moves:
                parent.move(parent.cars[move[0]], move[1])

            if len(parent.steps) < depth - 1:
                 # Retrieve children from parent and set new depth limit if game is won
                children, winning_child = parent.get_children()
                if winning_child:
                    depth = len(parent.steps) + 1

                # Else append the unknown or better children to the stack
                for child in children:
                    if not child["matrix"] in archive or len(child["moves"]) < archive[child["matrix"]]:
                        archive[child["matrix"]] = len(child["moves"])
                        stack.append(child["moves"])
  
        if depth < initial_depth:
            print(depth)
            return
        initial_depth += 10
 
        
        
            