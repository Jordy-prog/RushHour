import copy
import re

def deepening(RushHour):
    depth = 0
    while True:
        stack = [RushHour]
        archive = {}
        archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)
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

