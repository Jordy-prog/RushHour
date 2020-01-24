import copy
import re


def dfs(RushHour):
    # Initial search depth
    initial_depth = 40

    while True:
        # Initialize archive and stack with the initial Rush hour in them
        archive = {}
        archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)
        stack = [RushHour.steps]
        depth = initial_depth
        print(depth)

        # Work through the queue and check all boards for solution
        while len(stack):
            # Take a parent from the back of the queue and move to boardstate
            parent_moves = stack.pop()
            parent = copy.deepcopy(RushHour)

            for move in parent_moves:
                parent.move(parent.cars[move[0]], move[1])

            # Makes sure new solution is better
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
  
        # Checks if best solution was found
        if depth < initial_depth:
            print(depth)
            return

        initial_depth += 10
 
        
        
            