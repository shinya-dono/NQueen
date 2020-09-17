from itertools import permutations
from Solution import Solution


class NQueensP(Solution):

    def solve(self):
        cols = range(self.size)
        for combo in permutations(cols, self.size):
            if self.size == len(set(combo[i] + i for i in cols)) == len(set(combo[i] - i for i in cols)):
                self.solutions += 1
                self.log(combo)
