# Programming theory: Rush Hour

Rush Hour is a sliding puzzle with a clear objective: move your red car to the exit of a 6x6 grid. However, other cars and trucks block the way. They can only be moved in their starting direction, so they cannot turn. The aim of this project is to solve Rush Hour with various algorithms to find the fastest way to leave the grid lock. Included in the project are three original 6x6 games, as well as three 9x9 and one 12x12 game.

## Installation

The required Python version for this project is 3.7 or higher.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to be able to install the Python packages.

```bash
pip install -r requirements.txt
```

## Usage

The program can be executed by entering the following command, in which the filename argument should correspond with one of the files in the "data" folder, e.g. 6x6_1.csv

```bash
python main.py <filename>
```

## Structure

The project is well structured, with all common files stored in the following folders. All the folders in /code contain a README.md with an explanation of what is present in the folder, to help the user navigate through the code.

* **/advanced** contains the write-up of the advanced section with several images
* **/data** contains the various gameboards in .csv files
* **/code** contains all Python files (.py)
  * **/code/algorithms** contains the code for executing the six algorithms, as well as a README.md with explanation of the algorithms.
  * **/code/classes** has the code for the two classes, and a README.md
  * **/code/modes** has the code for the three special game modes: plot, manual, and create board. It also has a README.md
* **/results** contains the most successful move set of the last run in a .csv file as well as an images folder. 
  * **/results/images** is a folder with results in picture format. These results are shown in the README.md of **/code/algorithms**

## Authors

Group Bigbrainz:

* Jordy Schifferstein
* Leon Besseling
* Yassin El-Baz

## Acknowledgements

We would like to thank the course coordinators and technical TA's (Marleen & Julien) with helping and providing guidance for this project.

## License

The project is licensed under the GNU GPLv3.
