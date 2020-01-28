import copy
import random
import re

from .helpers import execute_move_list


class BreadthFirst():
    """Class suitable for normal breadth first search and beam search.

    Methods:
        __init__: Sets the initial values to run the algorithm.
        update_archive: Adds all unknown boards to the archive.
        update_queue: Adds a selection (depending on beam search or normal bfs) to queue.
        run: Executes the algorithm in a loop.
    """

    def __init__(self, RushHour, beam):
        """Init function to initialize variables

        Parameters:
            RushHour (object): The original Rush Hour board.
            beam (int or None): If given, the amount of children let through with beam search.
        """
        self.archive = set()
        self.archive.add(re.sub(', ', '', str(RushHour.matrix)))
        self.queue = [RushHour.steps]
        self.curr_depth = 0
        self.beam = beam
        self.RushHour = RushHour
        self.solution = []
    
    def update_archive(self, children):
        """Adds children to archive if they are unknown.
        
        Parameters:
            children (list): List of children that need evaluation.

        Returns:
            new_children (list): List of children that were unknown and added to archive.
        """
        new_children = []
        for child in children:
            if not child["matrix"] in self.archive:
                self.archive.add(child["matrix"])
                new_children.append(child)
        return new_children

    def update_queue(self, children):
        """Adds children to queue. If a beam limit is present, that amount of children
        are added to the queue. If not, all children are added.
        
        Parameters:
            children (list): List of children that can be added to queue.
        """
        beam = len(children)
        if self.beam:
            beam = self.beam
            random.shuffle(children)
        i = 0

        while len(children) and i < beam:
            self.queue.append(children.pop()["moves"])
            i += 1

    def run(self):
        """Runs the breadth first search until a solution is found."""
        while len(self.queue):
            # Generate parent from move list by executing moves
            parent = copy.deepcopy(self.RushHour)
            move_list = self.queue.pop(0)
            parent = execute_move_list(parent, move_list)

            # Generate children, check if game is won, then update archive and queue
            children, winning_child = parent.get_children()

            if winning_child:
                self.solution = winning_child
                print(self.solution)
                break

            new_children = self.update_archive(children)
            self.update_queue(new_children)

            # if the algorithm goes a layer deeper, inform user
            if len(parent.steps) > self.curr_depth:
                self.curr_depth += 1
                print(self.curr_depth)