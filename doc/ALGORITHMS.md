# Possible algorithms

Note that for each algorithms, cars should not be able to move back and forwards.

## Semi-Random

This first algorithm aims to solve the Rush Hour game semi-randomly. To prevent a loop, this algorithm isn't fully random.

1. Move red car forward as far as possible.
2. Move a random car as far as possible. If both directions are possible: select random direction. 
3. Repeat until red car reaches exit.

## Furthest move

This algorithm aims to solve the Rush Hour game by selecting a car that can move the furthest.

1. Move red car forward as far as possible.
2. Move the car that can move the furthest. If more than one car can move this distance: select random car.
3. Repeat until red car reaches exit.

Note: It can be that this algorithm results in a loop without progressing the red car.

## Free-up

This algorithm aims to solve the Rush Hour game by counting how many cars would be free to move after all possible moves from the current board composition. Afterwards, it executes this move.

1. Identify all moves for all cars.
2. Count how many cars would be free to move after all these moves.
3. Make the move with the most free cars afterwards.
...

## Obstacle chain: from red car

This algorithm aims to solve the Rush Hour game by moving the red car as far as possible. Then, it tries to move the car directly in front of the red car. If this isn't possible, try to move the blocked car that blocks the red car. Move up this 'blocked car chain' to eventually move the last car in the chain and move all other cars. 

1. Move red car forward as far as possible.
2. Try to move the car directly in front of the red car. If it moves, go back to step 1.
3. Try to move the car in front or behind the previously blocked car. If it cannot move, repeat step 3. If it can move, go to step 1 again.

## Obstacle chain: from exit

Similair to the previous algorithm, but this algorithm aims to solve the puzzle by looking at which car blocks the exit and moving up the blocked car chain.

1. Move red car forward as far as possible.
2. Try to move the car directly in front of the exit. If it moves, go back to step 1.
3. Try to move the car in front or behind the previously blocked car. If it cannot move, repeat step 3. If it can move, go to step 1 again.

## Ideal situation

Figure out for each car that is in the way of the red car, where it can go to clear the path of the red car. Use the obstacle chain algorithm to move this car over there.