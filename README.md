# Programming theory: Rush Hour

Rush Hour is a sliding puzzle with a clear objective: move your red car to the exit of a 6x6 grid. However, other cars and trucks block the way. They can only be moved in their starting direction, so they cannot turn. The aim of this project is to solve Rush Hour with various algorithms to find the fastest way to leave the grid lock. Included in the project are three original 6x6 games, as well as three 9x9 and one 12x12 game.

## Installation

The required Python version for this project is 3.7 or higher.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to be able to install the Python packages.

```
pip install -r requirements.txt
```

## Usage

The program can be executed by entering the following command, in which the filename argument should correspond with one of the files in the "data" folder, e.g. 6x6_1.csv

```
python main.py <filename>
```

## Structure

The project is well structured, with all common files stored in the following folders:
* **/code**: contains all Python files (.py)
    * **/code/algorithms** contains the code for executing the six algorithms, and a README.md for elaboration
    * **/code/classes** has the code for the two classes
    * **/code/modes** has the code for the two special game modes: manual and plot
* **/data**: contains the various gameboards in .csv files

## Authors

* Jordy Schifferstein
* Leon Besseling
* Yassin El-Baz

## Acknowledgements

We would like to thank the course coordinators and technical TA's (Marleen & Julien) with helping and providing guidance for this project.

## License

Copyright (c) 2020 Leon Besseling, Jordy Schifferstein, Yassin El-Baz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
