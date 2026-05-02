
class MaxRisingPath:  # LeetCode Q.329.
    def __init__(self):
        self.matrix = []
        self.max_rising_path = []
        self.max_rising_len = 1

    def find_longest_rising_path(self, matrix: list[list[int]]) -> int:
        self.matrix = matrix

        # An entry's max rising path value is -1 if this entry is unsearched.
        # Otherwise, max rising path value is the finalized value w.r.t. entry.
        self.max_rising_path = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        self.max_rising_len = 1  # Base case.

        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                if self.max_rising_path[row_idx][col_idx] == -1:
                    self._dfs_rising_path(row_idx, col_idx)

        return self.max_rising_len

    def _dfs_rising_path(self, row_idx: int, col_idx: int) -> None:
        self.max_rising_path[row_idx][col_idx] = 1  # Base case: a path of only current entry.

        neighbors: list[tuple[int, int]] = [
            (row_idx + 1, col_idx), (row_idx - 1, col_idx),  # South & North.
            (row_idx, col_idx + 1), (row_idx, col_idx - 1)  # East & West.
        ]

        for neighbor_row_idx, neighbor_col_idx in neighbors:
            # Inbound checks on row & col indices.
            if not (0 <= neighbor_row_idx < len(self.matrix)): continue

            if not (0 <= neighbor_col_idx < len(self.matrix[0])): continue

            # Only consider neighbors that are bigger than current entry.
            if self.matrix[row_idx][col_idx] < self.matrix[neighbor_row_idx][neighbor_col_idx]:
                # Unsearched neighbor.
                if self.max_rising_path[neighbor_row_idx][neighbor_col_idx] == -1:
                    self._dfs_rising_path(neighbor_row_idx, neighbor_col_idx)

                rising_len = 1 + self.max_rising_path[neighbor_row_idx][neighbor_col_idx]

                if rising_len > self.max_rising_path[row_idx][col_idx]:
                    self.max_rising_path[row_idx][col_idx] = rising_len

                if rising_len > self.max_rising_len: self.max_rising_len = rising_len
