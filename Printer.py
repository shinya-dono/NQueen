class Printer:
    def __init__(self, size):
        self.draw_levels = ["show_blank_board", "show_short_board", "show_full_board"]
        self.size = size

    def show_blank_board(self, position):
        pass

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        """
        Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the corresponding row.
        """
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

    def print(self, level, positions):
        printer = getattr(self, self.draw_levels[level])
        printer(positions)

