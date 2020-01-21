import copy
import re

def deepening(RushHour):
    # Initialize depth and start algorithm
    depth = 0
    while True:
        # Initialize archive and stack with the initial Rush hour in them
        stack = [RushHour]
        archive = {}
        archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)

        # Work through the stack and check all boards for solution
        while len(stack) > 0:
            # Take a parent from the top of the stack
            parent = stack.pop()
    
            
            if len(parent.steps) < depth:
                for car in parent.cars.values():
                    free_space = car.look_around(parent)
                    for distance in range(free_space['front']):
                        child = copy.deepcopy(parent)
                        child.move(child.cars[car.name], distance + 1)
                        if child.game_won():
                            return True
                        board = re.sub(', ', '', str(child.matrix))
                        if board not in archive or len(child.steps) < archive[board]:
                            archive[board] = len(child.steps)
                            stack.append(child)

                    for distance in range(0, free_space['rear'], -1):
                        child = copy.deepcopy(parent)
                        child.move(child.cars[car.name], distance - 1)
                        if child.game_won():
                            return True
                        board = re.sub(', ', '', str(child.matrix))
                        if board not in archive or len(child.steps) < archive[board]:
                            archive[board] = len(child.steps)
                            stack.append(child)
        depth += 1
        print(depth)

