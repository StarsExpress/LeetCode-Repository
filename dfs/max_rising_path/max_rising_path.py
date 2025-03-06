
class MaxRisingPath:  # LeetCode Q.329.
    def __init__(self):
        self.matrix = []
        self.total_rows, self.total_cols = 0, 0
        self.longest_rising_lens = []
        self.max_rising_len = 1

    def find_longest_rising_path(self, matrix: list[list[int]]) -> int:
        self.matrix = matrix
        self.total_rows, self.total_cols = len(matrix), len(matrix[0])
        self.longest_rising_lens = [
            [0 for _ in range(self.total_cols)] for _ in range(self.total_rows)
        ]  # 0 denotes unsearched cell.
        self.max_rising_len = 1  # Base case.

        for row_idx in range(self.total_rows):
            for col_idx in range(self.total_cols):
                if self.longest_rising_lens[row_idx][col_idx] == 0:
                    self._dfs_max_rising_path(row_idx, col_idx)

        return self.max_rising_len

    def _dfs_max_rising_path(self, row_idx: int, col_idx: int) -> None:
        neighbors = []
        if col_idx < self.total_cols - 1:  # Can go East.
            neighbors.append((row_idx, col_idx + 1))

        if 0 < col_idx:  # Can go West.
            neighbors.append((row_idx, col_idx - 1))

        if row_idx < self.total_rows - 1:  # Can go South.
            neighbors.append((row_idx + 1, col_idx))

        if 0 < row_idx:  # Can go North.
            neighbors.append((row_idx - 1, col_idx))

        max_neighbor_len = 0
        for next_row_idx, next_col_idx in neighbors:
            neighbor = self.matrix[next_row_idx][next_col_idx]
            if neighbor > self.matrix[row_idx][col_idx]:
                if self.longest_rising_lens[next_row_idx][next_col_idx] == 0:
                    self._dfs_max_rising_path(next_row_idx, next_col_idx)

                neighbor_len = self.longest_rising_lens[next_row_idx][next_col_idx]
                if neighbor_len > max_neighbor_len:
                    max_neighbor_len = neighbor_len

        self.longest_rising_lens[row_idx][col_idx] = 1 + max_neighbor_len
        if self.longest_rising_lens[row_idx][col_idx] > self.max_rising_len:
            self.max_rising_len = self.longest_rising_lens[row_idx][col_idx]
