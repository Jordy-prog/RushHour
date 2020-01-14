import copy
from queue import Queue

def bfs(RushHour):
    archive = set()
    archive.add(hash(str(RushHour.matrix)))
    queue = Queue()
    queue.put(RushHour)
    
    while not queue.empty():
        parent = queue.get()
        for car in parent.cars.values():
            free_space = car.look_around(parent)
            for distance in range(free_space['front']):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], distance + 1)
                if child.game_won():
                    return True
                if hash(str(child.matrix)) not in archive:
                    archive.add(hash(str(child.matrix)))
                    queue.put(child)

            for distance in range(0, free_space['rear'], -1):
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], (distance - 1))
                if child.game_won():
                    return True
                if hash(str(child.matrix)) not in archive:
                    archive.add(hash(str(child.matrix)))
                    queue.put(child)