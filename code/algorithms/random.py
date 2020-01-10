import random
from ..classes import car
from time import sleep

def random_move(RushHour):
    while True:
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
        
        if free_rear or free_front:
            break

    distance = random.randrange(free_rear, free_front + 1)
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

def random_chain(RushHour):
    counter = 0
    obstacle_history = []
    while True:
        if counter == 0:
            previous_obstacle = None
            car = RushHour.cars['X']
        else:
            previous_obstacle = car
            car = obstacle

        counter += 1

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

        distance = 0

        if free_rear or free_front:
            # moves red car as far as possible, giving priority to forward movements
            if car == RushHour.cars['X']:
                if free_front:
                    distance = free_front
                else:
                    distance = free_rear
            else:
                while not distance:
                    distance = random.randrange(free_rear, free_front + 1) 
        
        if not (car, - distance) == RushHour.last_move and distance:
            break
        
        if car.direction == "H":
            car_front = RushHour.matrix[car.row][car.col + car.length] if car.col + car.length < RushHour.boardsize else None
            car_rear = RushHour.matrix[car.row][car.col - 1] if car.col - 1 >= 0 else None
        elif car.direction == "V":
            car_front = RushHour.matrix[car.row - car.length][car.col] if car.row - car.length >= 0 else None
            car_rear = RushHour.matrix[car.row + 1][car.col] if car.row + 1 < RushHour.boardsize else None
        
        obstacles = []
        for obstacle in [car_front, car_rear]:
            try:
                i = obstacle_history.index(car)
                if obstacle and not obstacle == obstacle_history[i + 1]:
                    obstacles.append(obstacle)
            except (ValueError, IndexError):
                if obstacle:
                    obstacles.append(obstacle)
        
        if not len(obstacles):
            break

        # CHECK WHICH OBSTACLE CAN MOVE

        obstacle = random.choice(obstacles)
        obstacle_history.append(obstacle)
        # print('obstacle:', obstacle)
        # sleep(0.5)

    # print('Car to move:', car)
    # sleep(0.5)
    RushHour.move(car, distance)

def random_chain_jordy(RushHour):
    counter = 0
    obstacle_history = []

    while True:
        if counter == 0:
            previous_obstacle = None
            car = RushHour.cars['X']
        else:
            previous_obstacle = car
            car = obstacle

        counter += 1

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

        distance = 0

        if free_rear or free_front:
            # moves red car as far as possible, giving priority to forward movements
            # if car == RushHour.cars['X']:
            #     if free_front:
            #         distance = free_front
            #     else:
            #         distance = free_rear
            # else:
            while not distance:
                distance = random.randrange(free_rear, free_front + 1)
        
        repetitive = False

        try:
            if car.moves[-2][0] == car.moves[-1][0] and car.moves[-2][1] == distance:
                repetitive = True

            if distance and not car.moves[-1][-1] == - distance and not repetitive:
                break
        except IndexError:
            break
        
        if car.direction == "H":
            car_front = RushHour.matrix[car.row][car.col + car.length + free_front] if car.col + car.length + free_front < RushHour.boardsize else None
            car_rear = RushHour.matrix[car.row][car.col + free_rear - 1] if car.col + free_rear - 1 >= 0 else None
        elif car.direction == "V":
            car_front = RushHour.matrix[car.row - car.length - free_front][car.col] if car.row - car.length - free_front >= 0 else None
            car_rear = RushHour.matrix[car.row - free_rear + 1][car.col] if car.row - free_rear + 1 < RushHour.boardsize else None

        obstacles = []
        for obstacle in [car_front, car_rear]:
            try:
                i = obstacle_history.index(car)
                
                if obstacle:
                    obstacles.append(obstacle)
            except (ValueError, IndexError):
                if obstacle:
                    obstacles.append(obstacle)

        if not len(obstacles):
            break

        # CHECK WHICH OBSTACLE CAN MOVE

        obstacle = random.choice(obstacles)
        obstacle_history.append(obstacle)
        # print('obstacle:', obstacle)
        # sleep(1)

    # print('Car to move:', car)
    
    car.add_move(distance)
    # sleep(2)
    RushHour.move(car, distance)
