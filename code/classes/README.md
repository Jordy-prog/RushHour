# Classes

The classes folder contains the car and board classes that are used as data structures for Rush Hour.

## Board

This Board class stores information of the board object. When a RushHour object is used throughout this project's code, it refers to the board class and its methods.

The methods within the board class are:

* __ **init** __: Intialize board variables.
* **load**: Load cars and initialize the matrix.
* **printboard**: Prints the current game board.
* **move**: Attempts to move the car.
* **get_children**: Determines which boards can be derived from the current board.
* **game_won**: Checks if the current game has been won.

---

## Car

This Car class stores information of a car object, sets it position on the game board and looks around to see if the car can move.

The methods within the car class are:

* __ **init** __: Intialize car variables.
* **set_position**: Setter method to set the position (col, row) for the car.
* **look_around**: Determines the free space in front and behind the car.
* __ **repr** __: Printable representation of the car name.
