import copy
import re


class bfs():
    def __init__(self, RushHour):
        self.archive = set()
        self.archive.add(re.sub(', ', '', str(RushHour.matrix)))
        self.queue = [RushHour.steps]
        self.curr_depth = 0
        self.RushHour = RushHour
        self.solution = []

    def next_parent_moves(self):
        # Take move list for parent from the front of the queue and execute moves
        return self.queue.pop(0)
    
    def update_parent(self, parent_moves):
        parent = copy.deepcopy(self.RushHour)

        for move in parent_moves:
            parent.move(parent.cars[move[0]], move[1])

        return parent
    
    def update_archive(self, children):
        for child in children:
            if not child["matrix"] in self.archive:
                self.archive.add(child["matrix"])
                self.queue.append(child["moves"])
    
    def run(self):
        while len(self.queue):
            next_parent = self.next_parent_moves()
            parent = self.update_parent(next_parent)
            children, winning_child = parent.get_children()

            if winning_child:
                self.solution = winning_child
                return True

            self.update_archive(children)

            if len(parent.steps) > self.curr_depth:
                self.curr_depth += 1
                print(self.curr_depth)