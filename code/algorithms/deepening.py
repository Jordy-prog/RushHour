import copy
from queue import Queue

def deepening(RushHour):
    
    depth = 0
    while depth < 30:
        stack = [RushHour]
        archive = {}
        archive[str(RushHour.matrix)] = len(RushHour.steps)
        maxstack = 0
        while len(stack) > 0:
            parent = stack.pop()
            if len(parent.steps) < depth:
                for car in parent.cars.values():
                    free_space = car.look_around(parent)
                    for distance in range(free_space['front']):
                        child = copy.deepcopy(parent)
                        child.move(child.cars[car.name], distance + 1)
                        if child.game_won():
                            return True
                        if str(child.matrix) not in archive or len(child.steps) < archive[str(child.matrix)]:
                            archive[str(child.matrix)] = len(child.steps)
                            stack.append(child)

                    for distance in range(0, free_space['rear'], -1):
                        child = copy.deepcopy(parent)
                        child.move(child.cars[car.name], distance - 1)
                        if child.game_won():
                            return True
                        if str(child.matrix) not in archive or len(child.steps) < archive[str(child.matrix)]:
                            archive[str(child.matrix)] = len(child.steps)
                            stack.append(child)
            if len(stack) > maxstack:
                maxstack = len(stack)
        depth += 1
        print(depth, len(archive))     

