"""
Printer class
performs arranging data and tries to visualise the board

you can add your custom output method by defining your method and adding its name to $draw_levels
your new method would be accessible by adding -d {index of your method in $draw_levels)
ex : py main.py 13 -ddd


* making those methods Private prevents from any call error
"""


class Printer:
    def __init__(self, size):
        # stores possible methods for modular calls
        self.draw_levels = ["__show_blank_board", "__show_short_board", "__show_full_board"]

        # store size for iterating
        self.size = size

    # shows nothing
    def __show_blank_board(self, position):
        pass

    # Show the full NxN board
    def __show_full_board(self, positions):

        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    """
          Show the queens positions on the board in compressed form,
          each number represent the occupied column position in the corresponding row.
    """
    def __show_short_board(self, positions):
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

    # only callable function from outside, used to execute printing sequence
    def print(self, level, positions):
        printer = getattr(self, self.draw_levels[level])
        printer(positions)
