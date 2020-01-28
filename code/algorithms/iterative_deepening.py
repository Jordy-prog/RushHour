import copy
import re

from .helpers import execute_move_list


class IterativeDeepening():
    """Class for iterative deepening.

    Methods:
        __init__: Sets the initial values to run the algorithm.
        update_archive_and_stack: Adds all unknown or better boards to the archive and stack.
        reset: Resets the stack and archive for a new iteration.
        search_to_layer: Searches through the three up untill the given depth.
        run: Executes the algorithm.
    """

    def __init__(self, RushHour):
        """Init function to initialize the variables, and to run the algorithm
        
        Parameters:
            RushHour (object): The original Rush Hour board.
        """
        self.archive = {}
        self.archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)
        self.stack = [RushHour.steps]
        self.RushHour = RushHour
        self.solution = []

    def update_archive_and_stack(self, children):
        """Adds children to archive if they are unknown, or if they are better.
        
        Parameters:
            children (list): List of children that need evaluation.
        """
        for child in children:
            if not child["matrix"] in self.archive or len(child["moves"]) < self.archive[child["matrix"]]:
                self.archive[child["matrix"]] = len(child["moves"])
                self.stack.append(child["moves"])

    def reset(self):
        """Setter method to clear the archive and stack."""
        self.archive = {}
        self.archive[re.sub(', ', '', str(self.RushHour.matrix))] = len(self.RushHour.steps)
        self.stack = [self.RushHour.steps]

    def search_to_layer(self, depth):
        """Starts a new search up until a specified layer of the tree.

        Parameters:
            depth (int): Dictates how deep the search may go.
        
        Returns:
            False (boolean): Solution wasn't found.
            True (boolean): Solution was found.
        """
        self.reset()

        while len(self.stack):
            parent = copy.deepcopy(self.RushHour)
            move_list = self.stack.pop()
            parent = execute_move_list(parent, move_list)

            if len(parent.steps) < depth:
                children, winning_child = parent.get_children()

                if winning_child:
                    self.solution = winning_child
                    return True

                self.update_archive_and_stack(children)

        return False

    def run(self):
        """Runs the iterative deepening algorithm. If a solution is not found within
        the depth limit, this limit is increased by 1.
        """
        depth = 0
        while True:
            depth += 1
            print("Now searching to depth:", depth)

            if self.search_to_layer(depth):
                print(self.solution)
                break