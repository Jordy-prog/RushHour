# Algorithms

## Random
#### Pure random
An almost pure random algorithm. The algorithm randomly picks a car on the board and tries to move it a random distance. The algorithm repeats this step over and over until it finds the solution.

We added one small heuristic for efficiency and clarity purposes. The algorithm uses a function to determine the free space around a car. Then the algorithm chooses a distance within the range that the car can move.

#### Constraint random
This algorithm is an adjustment to the purely random algorithm. It applies a few extra heuristics. First of all, if a car can move, the algorithm will keep randomly picking a distance until it picks a non-zero integer. Secondly, if the algorithm tries to move a car back to its previous position, this move is denied. This prevents the algorithm from moving cars back and forth. This second heuristic can in very rare occasions cause the algorithm to be stuck, if only one car can move, and it can’t undo its last move. So there is a failsave implemented that turns off this heuristic after a certain amount of moves.

A large disadvantage of the random algorithms is obviously that every outcome is different and that you can never know when you’ve found ‘the best solution’. 

---

## Hillclimb
Our hillclimb algorithm is focused on improving an already existing outcome. First, we take a random solution. Then the algorithm will take one slice out of the solution (which is just an order of moves), and will try to improve this. To improve a sequence, the algorithm uses random moves to achieve a boardstate that appears further in the original solution.
After the improvements we will run a procedure that we call: 'selective elimination'. This procedure checks if a boardstate appears multiple times in the moveset, and then removes everything in between.

An investigation that we did with our hillclimber is finding the best ratio between number of slices, number of improvements and the size of the slices.

INSERT TABLE WITH SOME RESULTS?

6x6_3.csv 100 runs

size slice 5 10 en 20
slices 5 20 100
improvements 5 20 100

---

## Breadth-first
The breadth-first search algorithm starts with the original board and derives all children of this board. A child is a board that can be created from the parent via a single move. All children are put at the end of the queue. The next parent to have its children analyzed is the first in line of the queue, thus the algorithm works with the first in first out (FIFO) principle. Therefore, the algorithm works down the tree one layer at a time. If a child is found that satisfies the winning condition, the algorithm ends.

Our breadth-first search makes use the archive to optimally prune, in which every new board that has been found is stored as a string. When this board is found again in another branch of the tree, it is not added to the queue, since its children are already in the queue from the first time this board was encountered.

The advantage of depth first is that the solution found is always in the shortest amount of steps. The disadvantage is that the queue grows exponentially, thus it requires a lot of memory to go deep into the tree.

---

## Depth-first
The depth-first search algorithm starts with the original board and derives all children of this board. All children are put at the end of the queue. The next parent to have its children analyzed is the last in line of the queue, thus the algorithm works with the last in first out (LIFO) principle. Therefore, the algorithm immediately dives deep into one branch of the tree, and can only come back up if it is stopped at a certain layer, or finds the solution. The depth-first algorithm also prunes optimally with the archive.

The advantage of depth first is that it 

---

## Iterative deepening
Iterative deepening combines breadth first search with depth first search. It is a depth search in which the depth to stop at is increased by one after every unsuccessful round. 
