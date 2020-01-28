from .iterative_deepening import IterativeDeepening as dfs


class BranchAndBound(dfs):

    def run(self):
        depth = 15
        while True:
            solution = self.solution
            print("Now searching to depth:", depth)
            
            if self.search_to_layer(depth):
                depth = len(self.solution) - 1
            else:
                depth += 5
            
            if len(self.solution) and len(self.solution) == len(solution):
                print(self.solution)
                return