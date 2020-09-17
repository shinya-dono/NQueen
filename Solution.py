from Printer import Printer


class Solution:
    def __init__(self, size, draw_level=0):
        self.solutions = 0
        self.size = size
        self.draw_level = draw_level
        self.Printer = Printer(size)
        self.solve()
        print("Found", self.solutions, "solutions.")

    # overwrite!
    def solve(self):
        raise NotImplementedError("Hey, you have to deploy your own solve method!")

    # overwrite at will
    def log(self, positions):
        self.Printer.print(self.draw_level, positions)