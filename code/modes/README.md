# Modes

The modes folder contains the car and board classes that are used as data structures for Rush Hour.

## Manual

The manual mode implements a manual gameplay variation of the Rushhour game.
When the user selects this mode, the user has to provide input for each move when playing.
This method uses the move and look_around method to play the game and continiously checks if the game has been won already.

---

## Plot

The plot game mode runs a certain algorithm a number of times, in order to plot the result(s) in a MatPlotLib graph.

This mode has only been implemented for a certain selection of algorithms, due to the time contraint.

* Random (pure/constraint) algorithm:
  * Histogram
* Hillclimb algorithm:
  * Histogram
  * Line graph
* Depth first search algorithm:
  * Line graph
