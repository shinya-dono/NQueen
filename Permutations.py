from itertools import permutations
from Solution import Solution

"""
    finds all Permutations of queens
    rejects invalid answers and reports them
"""


class NQueensP(Solution):

    def solve(self):
        # creates list of columns
        cols = range(self.size)
        # iterates the permutations list
        for combo in permutations(cols, self.size):
            # rejecting invalid answers
            if self.check_place(combo):
                # updating $self.solutions
                self.solutions += 1
                # logging the solution
                self.log(combo)

    def check_place(self, positions):
        """
            its a permutation so we can assume that we are not going to have queens in same row/column
            only problem remaining is diagonal attack
            which we can check by calculating line formula of each diagonal attack line (y = ax + b)
            same line formula means that two queens are in the same diagonal and are in attack position

            so if we gather them all in a tuple (which does not accept duplicate values) and count them
            we can determine if two queens have same line formula by comparing their count to queens count!!
        """
        return self.size == len(set(positions[i] + i for i in range(self.size))) == len(
            set(positions[i] - i for i in range(self.size)))
