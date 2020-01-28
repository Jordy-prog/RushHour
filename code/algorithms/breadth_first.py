import copy
import random
import re


class BreadthFirst():
    """Class suitable for normal breadth first search and beam search.

    Methods:
        __init__: sets the initial values to run the algorithm.
        next_parent: takes the first item from the queue.
        update_parent: executes a list of moves onto the default board.
        update_archive: adds all unknown boards to the archive.
        update_queue: adds a selection (depending on beam search or normal bfs) to queue.
        run: executes the algorithm in a loop.
    """

    def __init__(self, RushHour, beam):
        """Init function to initialize variables

        Parameters:
            RushHour (object): the original Rush Hour board
            beam (int or None): amount of children let through per parent. In case of None,
                all children are let through
        """
        self.archive = set()
        self.archive.add(re.sub(', ', '', str(RushHour.matrix)))
        self.queue = [RushHour.steps]
        self.curr_depth = 0
        self.beam = beam
        self.RushHour = RushHour
        self.solution = []

    def next_parent(self):
        """Take the next parent's move list from the front of the queue
        
        Returns:
            
        """
        return self.queue.pop(0)
    
    def update_parent(self, parent_moves):
        parent = copy.deepcopy(self.RushHour)

        for move in parent_moves:
            parent.move(parent.cars[move[0]], move[1])

        return parent
    
    def update_archive(self, children):
        new_children = []
        for child in children:
            if not child["matrix"] in self.archive:
                self.archive.add(child["matrix"])
                new_children.append(child)
        return new_children


    def update_queue(self, children):
        beam = len(children)
        if self.beam:
            beam = self.beam
            random.shuffle(children)
        i = 0

        while len(children) and i < beam:
            self.queue.append(children.pop()["moves"])
            i += 1

    def run(self):
        while len(self.queue):
            next_parent = self.next_parent()
            parent = self.update_parent(next_parent)
            children, winning_child = parent.get_children()

            if winning_child:
                self.solution = winning_child
                return True

            new_children = self.update_archive(children)
            self.update_queue(new_children)

            if len(parent.steps) > self.curr_depth:
                self.curr_depth += 1
                print(self.curr_depth)