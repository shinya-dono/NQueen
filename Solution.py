from Printer import Printer

"""
abstract class

all of solutions must follow this abstract in order to follow bot Single Responsibility Principle
and Interface Segregation Principle (idk if we have those in Python i'm from PHP :| ) 
"""


class Solution:
    def __init__(self, size, draw_level=0):
        # stores total count of valid solutions
        self.solutions = 0
        # storing board size
        self.size = size
        # storing draw level used in printer class
        self.draw_level = draw_level
        # Printer instance
        self.Printer = Printer(size)

        # solving the puzzle (update $self.solutions
        self.solve()
        # reporting count of solutions
        print("Found", self.solutions, "solutions.")

    # overwrite!
    # method has to be overwritten and update $self.solutions and log the solution for each valid solution found
    def solve(self):
        raise NotImplementedError("Hey, you have to deploy your own solve method!")

    # overwrite at will
    def log(self, positions):
        """
            logging the solution, you can implement your logic here to log only certain solutions
            (ex: solutions with the queen in row 5)
        """
        self.Printer.print(self.draw_level, positions)
