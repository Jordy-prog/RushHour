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

    # print(queue.qsize())
    # print(len(children))

#     else:
#         for child_to_check in children:
#             for car in child_to_check.cars.values():
#                 free_space = car.look_around(RushHour)
#                 for distance in range(free_space['front']):
#                     child = copy.deepcopy(original)
#                     child.move(car, distance + 1)
#                     if child.game_won():
#                         print("CONGRATULATIONS)")
#                         break
#                     children.append(child)
#                 for distance in range(0, free_space['rear'], -1):
#                     child = copy.deepcopy(original)
#                     child.move(car, distance - 1)
#                     if child.game_won():
#                         print("CONGRATULATIONS)")
#                         break
#                     children.append(child)




# Startpunt:
#  - voor elke auto in bord.cars : car.lookaround. 
#     - for i in car.freerear
#         nieuwbord = copy.deepcopy(vorigbord)
#         nieuwbord.move(car, i)
#         if nieuwbord.game_won():
#             break
#         queue.append(nieuwbord)
#     - for i in car.freefront
#         nieuwbord = copy.deepcopy(vorigbord)
#         nieuwbord.move(car, i)
#         if nieuwbord.game_won():
#             break
#         queue.append(nieuwbord)