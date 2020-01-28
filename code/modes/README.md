# Modes

The modes folder contains the game modes that can be used to run the game.

## Advanced

The create board mode is responsible for creating a random board and shuffling it. These boards are always solvable. The function saves the board in a csv file in the data folder, under the filename provided as argument. Be careful not to overwrite existing boards, unless you intend to do so. Example to create a board named 6x6_test.csv:

```bash
python main.py 6x6_test.csv
```
Then select the create board mode.

---

## Manual

The manual mode implements a manual gameplay variation of the Rushhour game. When the user selects this mode, the user has to provide input for each move when playing.

---

## Plot

The plot mode runs a certain algorithm a number of times, in order to plot the result(s) in a MatPlotLib graph.

This mode has only been implemented for a certain selection of algorithms for which plotting the results renders interesting graphics.

* Random pure and random constraint: Histogram
* Random branch and bound: Line graph
* Hillclimb algorithm: Line graph

