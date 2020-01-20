import copy
import re
import random

def bfs_beam(RushHour):
    archive = set()
    archive.add(re.sub(', ', '', str(RushHour.matrix)))
    queue = []
    queue.append(RushHour)
    beam = 2
    current_depth = 0
    while len(queue):
        parent = queue.pop(0)
        children = []
        for car in parent.cars.values():
            free_space = car.look_around(parent)
            for distance in range(free_space['front']):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], distance + 1)
                if child.game_won():
                    return True
                string = re.sub(', ', '', str(child.matrix))
                if string not in archive:
                    archive.add(string)
                    children.append(child)
            
            for distance in range(0, free_space['rear'], -1):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], (distance - 1))
                if child.game_won():
                    return True
                string = re.sub(', ', '', str(child.matrix))
                if string not in archive:
                    archive.add(string)
                    children.append(child)

        i = 0
        while len(children) and i < beam:
            index = random.randint(0, len(children))
            queue.append(children.pop(index - 1))
            i += 1

        if len(parent.steps) > current_depth:
            current_depth += 1 
            print(current_depth)
        
        
            