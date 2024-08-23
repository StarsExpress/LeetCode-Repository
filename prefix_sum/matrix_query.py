
class Matrix:  # LeetCode Q.304.
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        for row_idx, row in enumerate(self.matrix):
            for col_idx, entry in enumerate(row):
                if col_idx > 0:  # Not 1st column: inherit from left side neighbor.
                    self.matrix[row_idx][col_idx] += self.matrix[row_idx][col_idx - 1]

            if row_idx > 0:  # Not 1st row: inherit from upper neighbor.
                for col_idx, entry in enumerate(row):
                    self.matrix[row_idx][col_idx] += self.matrix[row_idx - 1][col_idx]

    def query_sum(self, row_idx_1: int, col_idx_1: int, row_idx_2: int, col_idx_2: int):
        prefix_sum = self.matrix[row_idx_2][col_idx_2]
        if row_idx_1 > 0:  # Upper deduction.
            prefix_sum -= self.matrix[row_idx_1 - 1][col_idx_2]
        if col_idx_1 > 0:  # Left side deduction.
            prefix_sum -= self.matrix[row_idx_2][col_idx_1 - 1]

        # When "both" deductions happen: add back left upper area that is deducted twice.
        if min(row_idx_1, col_idx_1) > 0:
            prefix_sum += self.matrix[row_idx_1 - 1][col_idx_1 - 1]
        return prefix_sum
