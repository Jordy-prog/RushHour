from .iterative_deepening import IterativeDeepening as dfs


class BranchAndBound(dfs):
    """Class for branch and bound. Since all the functions are equal to iterative
        deepening, the IterativeDeepening class is used as a parent.
    
    Methods:
        run: executes the algorithm
    """

    def run(self):
        """Runs the branch and bound algorithm. If a solution is not found within
            the initial depth, this limit is increased by 5. If a solution is found, 
            depth is lowered by 1 until no better solution can be found.
        """
        depth = 15
        while True:
            solution = self.solution
            print("Now searching to depth:", depth)
            
            if self.search_to_layer(depth):
                depth = len(self.solution) - 1
            else:
                depth += 5
            
            # The algorithm can stop if the length of 
    
            if len(self.solution) and len(self.solution) == len(solution):
                print(self.solution)
                break