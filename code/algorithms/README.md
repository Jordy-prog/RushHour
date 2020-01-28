# Algorithms

The algorithms folder contains the algorithms that can be used to solve a Rush Hour board. This file explains them briefly.

## Random

### Pure random

The algorithm randomly picks a car on the board, then checks how far the car can move forwards or backwards and picks a random number in this range. This is repeated until it finds the solution.

### Constraint random

This algorithm applies a heuristic to improve the random. If the picked random car and distance are opposite of the previous move, this move is denied. This can in very rare occasions cause the algorithm to be stuck: if only one car can move, it can’t undo its last move. So there is a failsave implemented that turns off this heuristic after a certain amount of moves.

An advantage of the random algorithms is that they find a solution quickly. A large disadvantage of the random algorithms is that you can never know if a solution is the shortest possible.

#### Branch and bound random
This algorithm builds upon the constraint random. It runs that algorithm multiple times, keeping track of the shortest solution. If a next iteration uses more steps than this known shortest solution, the iteration is stopped. The advantage of this heuristic is that you randomly walk towards the best solution. This results in a better estimation of the best solution instead of completely random solutions.

---

## Hillclimb

Our hillclimb algorithm is focused on improving an already existing outcome. First, we take a random solution. Then the algorithm will take one slice out of the solution (which is just an order of moves), and will try to improve this. To improve a sequence, the algorithm uses random moves to achieve a boardstate that appears further in the original solution.
After the improvements we will run a procedure that we call: 'selective elimination'. This procedure checks if a boardstate appears multiple times in the moveset, and then removes everything in between.

An investigation that we did with our hillclimber is finding the best ratio between number of slices, number of improvements and the size of the slices.

INSERT TABLE WITH SOME RESULTS?

| |
|
|
|
|

6x6_3.csv 100 runs

size slice 5 10 en 20
slices 5 20 100
improvements 5 20 100

---

## Breadth First Search (BFS)

The breadth first search algorithm starts with the original board and derives all children of this parent board. A child is a board that can be created from the parent via a single move. All children are put at the end of the queue. The next parent to have its children analyzed is the first in line of the queue, thus the algorithm works with the first in first out (FIFO) principle. Therefore, the algorithm works down the tree one layer at a time. If a child is found that satisfies the winning condition, the algorithm ends.

Our BFS makes use of the archive to optimally prune, in which every new board that has been found is stored as a string. When this board is found again in another branch of the tree, it is not added to the queue, since its children are already in the queue from the first time this board was encountered.

The advantage of breadth first is that the solution found is always in the shortest amount of steps. The disadvantage is that the queue grows exponentially, thus it requires a lot of memory to go deep into the tree.

---

## Depth First Search (DFS)

The depth first search algorithm starts with the original board and derives all children of this board. All children are put at the end of the queue. The next parent to have its children analyzed is the last in line of the queue, thus the algorithm works with the last in first out (LIFO) principle. Therefore, the algorithm immediately dives deep into one branch of the tree, and can only come back up if it is stopped at a certain layer, or finds the solution. The depth-first algorithm also prunes optimally with the archive.

The advantage of depth first is that this algorithm takes up much less memory (RAM) than breadth first.

---

## Iterative deepening

Iterative deepening combines breadth first search with depth first search. It is a depth search in which the depth to stop at is increased by one after every unsuccessful round.

[LEON]

---

## Breadth First Search: Beam search

Beam search is a variation on Breadth First Search. With Beam search, the amount of children for each parent will be contrained by a number (2 or 3 in our case), instead of exploring each child like you would do in a BFS algorithm.

With beam search, the algorithm isn't guaranteed to find a solution (winning board). A larger beam number will result in a higher chance to find a solution, but it will be much slower to traverse the tree. A smaller beam number will result in a faster way to traverse the tree, but will decrease the chances to find a solution.
