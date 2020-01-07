# Process

This file aims to provide insight in the progression of this project. Each day, there will be a short write-up on what has been done and which challenges we faced individually and collectively.

## 6 january 2020

On the first day we immersed ourselves in the Rush Hour case. We played a few games of Rush Hour and got a good understanding what kind of challenges we would face if we tried to program a Rush Hour solving algorithm.

Tasks done:

* Programmed a matrix (essentially a list of lists) in Python; each point/letter represents (part of) a car/truck. 
* Brainstorm session on which algorithms would be useful to solve a Rush Hour game.

Challenges faced & discovered:

* When should the algorithm move the red car backwards?
* Should we implement a log/memory feature to remember the moves of the car?

Eventually we realized we have to verify the output in a uniform manner.

## 7 january 2020

We presented our progress in the work group and received as feedback:
"You shouldn't store information double. You are storing the coordinates in the matrix and Car objects."

We decided to store the information on two places, the Car objects and matrix. The reason behind this principle is we want to remember the car object position simply in a Car object and not to loop through the matrix to find out where the car is situated on the board.

Tasks done:

* Move class/feature is being worked on, mainly by Jordi
* Brainstorming about the structure of the code (how to separate logic in different files)
* Pseudocode for different algorithms is being worked on by Leon and Yassin

Challenges faced & discovered:
* When should the algorithm move the red car backwards?
