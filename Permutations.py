from itertools import permutations
from Solution import Solution


class NQueensP(Solution):

    def solve(self):
        cols = range(self.size)
        for combo in permutations(cols, self.size):
            if self.check_place(combo):
                self.solutions += 1
                self.log(combo)

    def check_place(self, positions):
        return self.size == len(set(positions[i] + i for i in range(self.size))) == len(set(positions[i] - i for i in range(self.size)))
