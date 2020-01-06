# Possible algorithms
Note that for each algorithms, cars should not be able to move back and forwards.

### Random
1. Move red car forward as far as possible.
2. Move a random car as far as possible. If both directions are possible: select random direction. 
3. Repeat until red car reaches exit.

### Furthest move
1. Move red car forward as far as possible.
2. Move the car that can move the furthest. If more than one car can move this distance: select random car.
3. Repeat until red car reaches exit.

Note: It can be that this algorithm results in a loop without progressing the red car.

### Free-up
1. Identify all moves for all cars.
2. Count how many cars would be free to move after all these moves.
3. Make the move with the most free cars afterwards.

### Obstacle chain: from red car
1. Move red car forward as far as possible.
2. Try to move the car directly in front of the red car. If it moves, go back to step 1.
3. Try to move the car in front or behind the previously blocked car. If it cannot move, repeat step 3. If it can move, go to step 1 again.

### Obstacle chain: from exit
1. Move red car forward as far as possible.
2. Try to move the car directly in front of the exit. If it moves, go back to step 1.
3. Try to move the car in front or behind the previously blocked car. If it cannot move, repeat step 3. If it can move, go to step 1 again.

### Ideal situation
Figure out for each car that is in the way of the red car, where it can go to clear the path of the red car. Use the obstacle chain algorithm to move this car over there.