import copy
from queue import Queue
from time import sleep
from collections import OrderedDict

def bfs(RushHour):
    archive = set()
    queue = Queue()
    queue.put(RushHour)
    solution = False
    
    while not solution and not queue.empty():
        parent = queue.get()
        for car in parent.cars.values():
            free_space = car.look_around(parent)
            for distance in range(free_space['front']):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], distance + 1)
                if child.game_won():
                    solution = True
                if str(child.matrix) not in archive:
                    archive.add(str(child.matrix))
                    queue.put(child)

            for distance in range(0, free_space['rear'], -1):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], (distance - 1))
                if child.game_won():
                    solution = True
                if str(child.matrix) not in archive:
                    archive.add(str(child.matrix))
                    queue.put(child)