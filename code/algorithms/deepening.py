import copy
import re

def deepening(RushHour):
    # Initialize depth and start algorithm
    depth = 0
    while True:
        # Initialize archive and stack with the initial Rush hour in them
        stack = [RushHour.steps]
        archive = {}
        archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)

        # Work through the stack and check all boards for solution
        while len(stack) > 0:
            # Take a parent from the top of the stack
            parent_moves = stack.pop()
            parent = copy.deepcopy(RushHour)
            for move in parent_moves:
                parent.move(parent.cars[move[0]], move[1])
    
            if len(parent.steps) < depth:
                for car in parent.cars.values():
                    free_space = car.look_around(parent)
                    for distance in range(free_space['front']):
                        # Create a copy for the child and move the car
                        parent.move(car, distance + 1)
                        
                        # Return True if this child results in a win
                        if parent.game_won():
                            return True
                        last_move = parent.steps.pop() 

                        # Only add unknown boards to the archive and to the queue (optimal pruning)
                        board = re.sub(', ', '', str(parent.matrix))
                        if board not in archive or len(parent.steps) < archive[board]:
                            archive[board] = len(parent.steps)
                            move_list = parent_moves + [last_move]
                            stack.append(move_list)

                        # Undo move to bring parent back to original state
                        parent.move(car, - (distance + 1))
                        parent.steps.pop()

                    for distance in range(0, free_space['rear'], -1):
                        parent.move(car, (distance - 1))

                        if parent.game_won():
                            return True
                        last_move = parent.steps.pop()

                        board = re.sub(', ', '', str(parent.matrix))
                        if board not in archive or len(parent.steps) < archive[board]:
                            archive[board] = len(parent.steps)
                            move_list = parent_moves + [last_move]
                            stack.append(move_list)

                        parent.move(car, - (distance - 1))
                        parent.steps.pop()

        depth += 1
        print(depth)
        

