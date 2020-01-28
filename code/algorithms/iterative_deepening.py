import copy
import re


class IterativeDeepening():
    def __init__(self, RushHour):
        self.archive = {}
        self.archive[re.sub(', ', '', str(RushHour.matrix))] = len(RushHour.steps)
        self.stack = [RushHour.steps]
        self.RushHour = RushHour
        self.solution = []
        self.run()

    def next_parent(self):
        # Take move list for parent from the bsck of the queue and execute moves
        return self.stack.pop()

    def update_parent(self, parent_moves):
        parent = copy.deepcopy(self.RushHour)

        for move in parent_moves:
            parent.move(parent.cars[move[0]], move[1])

        return parent

    def update_archive_and_stack(self, children):
        for child in children:
            if not child["matrix"] in self.archive or len(child["moves"]) < self.archive[child["matrix"]]:
                self.archive[child["matrix"]] = len(child["moves"])
                self.stack.append(child["moves"])

    def reset(self):
        self.archive = {}
        self.archive[re.sub(', ', '', str(self.RushHour.matrix))] = len(self.RushHour.steps)
        self.stack = [self.RushHour.steps]

    def search_to_layer(self, depth):
        self.reset()

        while len(self.stack):
            next_parent = self.next_parent()
            parent = self.update_parent(next_parent)

            if len(parent.steps) < depth:
                children, winning_child = parent.get_children()

                if winning_child:
                    self.solution = winning_child
                    return True

                self.update_archive_and_stack(children)

        return False

    def run(self):
        depth = 0
        while True:
            depth += 1
            print("Now searching to depth:", depth)

            if self.search_to_layer(depth):
                print(self.solution)
                return