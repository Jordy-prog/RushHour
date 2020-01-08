import random
from objects import Car

def random_move(RushHour):
    # move(self, car, distance)
    car = random.choice(list(RushHour.cars.values()))
    free_rear = 
    free_front =
    

    distance = random.randrange(car.free_rear, car.free_front + 1)
    RushHour.move(car, distance, )


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


