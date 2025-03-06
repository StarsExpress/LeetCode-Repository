
class RisingWater:  # LeetCode Q.778.
    def __init__(self):
        self.water: list[list[int]] = []
        self.total_rows, self.total_cols = 0, 0
        self.visited_cells = set()  # Format: str(row idx) + ":" + str(col idx).

    def swim(self, water: list[list[int]]) -> int:
        self.water.clear()
        self.water.extend(water)
        self.total_rows, self.total_cols = len(water), len(water[0])
        bottom_right_cell_id = f"{self.total_rows - 1}:{self.total_cols - 1}"

        min_elevation, max_elevation = water[0][0], max(sum(self.water, []))
        while min_elevation <= max_elevation:
            mid_elevation = (min_elevation + max_elevation) // 2

            self.visited_cells.clear()  # Reset before DFS.
            self._dfs_path(0, 0, mid_elevation)
            if bottom_right_cell_id in self.visited_cells:
                max_elevation = mid_elevation - 1
                continue
            min_elevation = mid_elevation + 1

        return min_elevation

    def _dfs_path(self, row_idx: int, col_idx: int, elevation: int) -> None:
        self.visited_cells.add(f"{row_idx}:{col_idx}")
        neighbors = [
            (row_idx, col_idx - 1), (row_idx, col_idx + 1),
            (row_idx - 1, col_idx), (row_idx + 1, col_idx)
        ]

        for neighbor_row_idx, neighbor_col_idx in neighbors:
            if not 0 <= neighbor_row_idx < self.total_rows:
                continue
            if not 0 <= neighbor_col_idx < self.total_cols:
                continue

            if self.water[neighbor_row_idx][neighbor_col_idx] <= elevation:
                neighbor_id = f"{neighbor_row_idx}:{neighbor_col_idx}"
                if neighbor_id not in self.visited_cells:
                    self._dfs_path(neighbor_row_idx, neighbor_col_idx, elevation)
