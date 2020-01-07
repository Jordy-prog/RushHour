import random


def random():
    car = random.choice(list(cars.values()))
    if car.front_distance > 0 or car.rear_distance > 0: ## IN EEN REGEL ???? OF MET ELIF ????
        RushHour.move(car)
    elif car.rear_distance > 0:
        RushHour.move(car)


def obstacle_chain():
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


