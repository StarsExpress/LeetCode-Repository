
class RisingPaths:  # LeetCode Q.2328.
    def __init__(self):
        self.grid = []
        self.total_rows, self.total_cols = 0, 0
        self.modulo = 10 ** 9 + 7

        self.rising_paths = []  # Number of rising paths starting at each cell.
        self.total_rising_paths = 0

    def count_rising_paths(self, grid: list[list[int]]) -> int:
        self.grid.clear()  # Reset before DFS.
        self.grid.extend(grid)
        self.total_rows, self.total_cols = len(grid), len(grid[0])

        self.rising_paths.clear()
        self.rising_paths.extend(
            [[None] * self.total_cols for _ in range(self.total_rows)]
        )

        self.total_rising_paths = 0
        for row_idx in range(self.total_rows):
            for col_idx in range(self.total_cols):
                if not self.rising_paths[row_idx][col_idx]:  # Cell hasn't done DFS.
                    self._dfs_rising_paths(row_idx, col_idx)

        return self.total_rising_paths

    def _dfs_rising_paths(self, row_idx: int, col_idx: int) -> None:
        rising_paths_count = 1  # Base case: path of only the current cell.

        if col_idx < self.total_cols - 1:  # Go East if available.
            if self.grid[row_idx][col_idx] < self.grid[row_idx][col_idx + 1]:
                if not self.rising_paths[row_idx][col_idx + 1]:
                    self._dfs_rising_paths(row_idx, col_idx + 1)
                rising_paths_count += self.rising_paths[row_idx][col_idx + 1]

        if 0 < col_idx:  # Go West if available.
            if self.grid[row_idx][col_idx] < self.grid[row_idx][col_idx - 1]:
                if not self.rising_paths[row_idx][col_idx - 1]:
                    self._dfs_rising_paths(row_idx, col_idx - 1)
                rising_paths_count += self.rising_paths[row_idx][col_idx - 1]

        if row_idx < self.total_rows - 1:  # Go South if available.
            if self.grid[row_idx][col_idx] < self.grid[row_idx + 1][col_idx]:
                if not self.rising_paths[row_idx + 1][col_idx]:
                    self._dfs_rising_paths(row_idx + 1, col_idx)
                rising_paths_count += self.rising_paths[row_idx + 1][col_idx]

        if 0 < row_idx:  # Go North if available.
            if self.grid[row_idx][col_idx] < self.grid[row_idx - 1][col_idx]:
                if not self.rising_paths[row_idx - 1][col_idx]:
                    self._dfs_rising_paths(row_idx - 1, col_idx)
                rising_paths_count += self.rising_paths[row_idx - 1][col_idx]

        self.rising_paths[row_idx][col_idx] = rising_paths_count % self.modulo
        self.total_rising_paths += self.rising_paths[row_idx][col_idx]
        self.total_rising_paths %= self.modulo
