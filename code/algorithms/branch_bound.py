from .iterative_deepening import IterativeDeepening as dfs
from .helpers import write_csv


class BranchAndBound(dfs):
    """Class for branch and bound. Since all the functions are equal to iterative
        deepening, the IterativeDeepening class is used as a parent.
    
        Methods:
            run: Executes the algorithm.
    """

    def run(self):
        """Runs the branch and bound algorithm. If a solution is not found within
            the initial depth, this limit is increased by 5. If a solution is found, 
            depth is lowered by 1 until no better solution can be found. 
        """
        depth = 30
        while True:
            solution = self.solution
            print("Now searching to depth:", depth)

            if self.search_to_layer(depth):
                depth = len(self.solution) - 1
            else:
                depth += 5
            
            # The algorithm stops if the length of the solution did not change anymore
            if len(self.solution) and len(self.solution) == len(solution):
                print("No solution found at this depth. The best solution is:")
                print(self.solution)
                break

        write_csv(self.solution)
        
