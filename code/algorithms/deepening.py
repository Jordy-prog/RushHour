import copy
from queue import Queue

def deepening(RushHour):
    archive = set()
    archive.add(hash(str(RushHour.matrix)))
    depth = 3
    stack = [RushHour]

    while len(stack) > 0:
        parent = stack.pop()
        if parent.steps < depth:
            for car in parent.cars.values():
                free_space = car.look_around(parent)
                for distance in range(free_space['front']):
                    child = copy.deepcopy(parent)
                    child.move(child.cars[car.name], distance + 1)
                    if child.game_won():
                        return True
                    if hash(str(child.matrix)) not in archive:
                        archive.add(hash(str(child.matrix)))
                        stack.append(child)

                for distance in range(0, free_space['rear'], -1):
                    child = copy.deepcopy(parent)
                    child.move(child.cars[car.name], (distance - 1))
                    if child.game_won():
                        return True
                    if hash(str(child.matrix)) not in archive:
                        archive.add(hash(str(child.matrix)))
                        stack.append(child)

