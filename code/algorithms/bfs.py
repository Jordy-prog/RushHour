
def bfs(RushHour):
    print(RushHour)
    pass

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