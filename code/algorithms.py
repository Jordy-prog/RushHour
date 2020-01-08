import random
from objects import Car

def random_move(RushHour):
    # move(self, car, distance)
    car = random.choice(list(RushHour.cars.values()))

    if car.direction == 'H':
        free_rear = 0
        for i in range(1, car.col + 1):
            if not RushHour.matrix[car.row][car.col - i]:
                free_rear -= 1
            else:
                break
        
        free_front = 0
        for i in range(1, RushHour.boardsize - (car.length - 1) - car.col):
            if not RushHour.matrix[car.row][car.col + (car.length - 1) + i]:
                free_front += 1
            else:
                break

    elif car.direction == 'V':
        free_rear = 0
        for i in range(1, RushHour.boardsize - car.row):
            if not RushHour.matrix[car.row + i][car.col]:
                free_rear -= 1
            else:
                break
        
        free_front = 0
        for i in range(1, car.row):
            if not RushHour.matrix[car.row - (car.length - 1) - i][car.col]:
                free_front += 1
            else:
                break
    
    car.freespace(free_front, free_rear)

    distance = random.randrange(car.free_rear, car.free_front + 1)
    RushHour.move(car, distance)


def obstacle_chain(RushHour):
    leader = cars['X']
    if leader.front_distance > 0:
        RushHour.move(leader)
    else:
        obstacle = RushHour.matrix[leader.row][leader.col + leader.length] # should be a car object
        while not RushHour.move(obstacle):
            if obstacle.direction == "H":
                car_front = RushHour.matrix[obstacle.row][obstacle.col + obstacle.length]
                car_rear = RushHour.matrix[obstacle.row][obstacle.col - 1]
            elif obstacle.direction == "V":
                car_front = RushHour.matrix[obstacle.row + obstacle.length][obstacle.col]
                car_rear = RushHour.matrix[obstacle.row - 1][obstacle.col]
            obstacle = random.choice([car_front, car_rear])


