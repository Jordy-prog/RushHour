import copy

def bfs_beam(RushHour):
    archive = set()
    archive.add(str(RushHour.matrix))
    queue = []
    queue.append(RushHour)
    beam = 2
    knowndepths = set()
    while len(queue):
        parent = queue.pop(0)
        child_counter = 0
        for car in parent.cars.values():
            if child_counter > beam:
                break
            free_space = car.look_around(parent)
            for distance in range(free_space['front']):
                if child_counter > beam:
                    break
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], distance + 1)
                if child.game_won():
                    return True
                if str(child.matrix) not in archive:
                    archive.add(str(child.matrix))
                    queue.append(child)
                    child_counter += 1
            
            for distance in range(0, free_space['rear'], -1):
                if child_counter > beam:
                    break
                child = copy.deepcopy(parent)
                child.move(child.cars[car.name], (distance - 1))
                if child.game_won():
                    return True
                if str(child.matrix) not in archive:
                    archive.add(str(child.matrix))
                    queue.append(child)
                    child_counter += 1
        if len(child.steps) not in knowndepths:
            knowndepths.add(len(child.steps))
            print(len(child.steps), len(queue))
        
        
            