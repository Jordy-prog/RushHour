import copy

def bfs_list(RushHour):
    start = copy.deepcopy(RushHour)
    archive = set()
    archive.add(str(RushHour.matrix))
    queue = []
    queue.append(RushHour)

    knowndepths = set()
    while len(queue):
        if len(queue) > 1:
            parent = copy.deepcopy(RushHour)
            move_list = queue.pop()
            for move in move_list:
                parent.move(parent.cars[move[0]], move[1])
        else:
            parent = copy.deepcopy(RushHour)
            
            
        for car in parent.cars.values():
            free_space = car.look_around(parent)
            for distance in range(free_space['front']):
                parent.move(car, distance + 1)
                if parent.game_won():
                    return True
                if str(parent.matrix) not in archive:
                    archive.add(str(parent.matrix))
                    queue.append(parent.steps)
                parent.move(car, - (distance + 1))
            
            for distance in range(0, free_space['rear'], -1):
                parent.move(car, (distance - 1))
                if parent.game_won():
                    return True
                if str(parent.matrix) not in archive:
                    archive.add(str(parent.matrix))
                    queue.append(parent.steps)
                parent.move(car, - (distance - 1))

        if len(parent.steps) not in knowndepths:
            knowndepths.add(len(parent.steps))
            print(len(parent.steps))
        
        
            