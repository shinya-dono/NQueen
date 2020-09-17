"""The n queens puzzle."""
from Solution import Solution


class NQueensR(Solution):
    """Generate all valid solutions for the n queens puzzle"""
    def solve(self):
        """Solve the n queens puzzle and print the number of solutions"""
        positions = {}
        self.put_queen(positions, 0)

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.log(positions)
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    @staticmethod
    def check_place(positions, taken_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(taken_rows):
            if positions[i] == column or \
                    positions[i] - i == column - taken_rows or \
                    positions[i] + i == column + taken_rows:
                return False
        return True


