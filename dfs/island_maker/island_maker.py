
class IslandMaker:  # LeetCode Q.827.
    def __init__(self):
        self.ocean: list[list[int]] = []
        self.total_rows, self.total_cols = 0, 0
        self.parents = dict()  # Keys: str(row idx) + ":" + str(col idx).
        self.island_sizes = dict()  # Keys: str(row idx) + ":" + str(col idx).
        self.largest_island = 1

    def discover_largest_island(self, ocean: list[list[int]]) -> int:
        self.ocean.clear()
        self.ocean = ocean
        self.total_rows, self.total_cols = len(ocean), len(ocean[0])

        self.parents.clear()  # Reset before DFS.
        self.island_sizes.clear()
        self.largest_island = 1  # Base case: the answer when no original islands exist.

        for row_idx in range(self.total_rows):
            for col_idx in range(self.total_cols):
                if self.ocean[row_idx][col_idx] == 1:  # Part of an original island.
                    cell_id = f"{row_idx}:{col_idx}"
                    if cell_id not in self.parents.keys():
                        self._dfs_island(row_idx, col_idx, f"{row_idx}:{col_idx}")

        if self.island_sizes:  # Some islands exist in the beginning.
            for row_idx in range(self.total_rows):
                for col_idx in range(self.total_cols):
                    if self.ocean[row_idx][col_idx] == 0:  # Wasn't island.
                        self._make_island(row_idx, col_idx)

        return self.largest_island

    def _dfs_island(self, row_idx: int, col_idx: int, parent_id: str) -> int:
        cell_id = f"{row_idx}:{col_idx}"
        self.parents.update({cell_id: parent_id})

        neighbors: list[tuple[int, int]] = []
        if col_idx < self.total_cols - 1 and self.ocean[row_idx][col_idx + 1] == 1:
            neighbors.append((row_idx, col_idx + 1))  # Can extend to East.

        if 0 < col_idx and self.ocean[row_idx][col_idx - 1] == 1:
            neighbors.append((row_idx, col_idx - 1))  # Can extend to West.

        if row_idx < self.total_rows - 1 and self.ocean[row_idx + 1][col_idx] == 1:
            neighbors.append((row_idx + 1, col_idx))  # Can extend to South.

        if 0 < row_idx and self.ocean[row_idx - 1][col_idx] == 1:
            neighbors.append((row_idx - 1, col_idx))  # Can extend to North.

        island_size = 1  # Start with current cell as the only island area.
        for neighbor_row_idx, neighbor_col_idx in neighbors:
            neighbor_id = f"{neighbor_row_idx}:{neighbor_col_idx}"
            if neighbor_id not in self.parents.keys():  # Not DFS yet.
                island_size += self._dfs_island(
                    neighbor_row_idx, neighbor_col_idx, parent_id
                )

        if cell_id == parent_id:  # Parent cells have to update island size.
            self.island_sizes.update({cell_id: island_size})
            if island_size > self.largest_island:
                self.largest_island = island_size

        return island_size

    def _make_island(self, row_idx, col_idx) -> None:
        island_size = 1  # Current cell now becomes island.

        neighbor_ids = [
            f"{row_idx}:{col_idx + 1}", f"{row_idx}:{col_idx - 1}",
            f"{row_idx + 1}:{col_idx}", f"{row_idx - 1}:{col_idx}"
        ]
        visited_parent_ids: set[str] = set()  # Visited parents of neighbors.
        for neighbor_id in neighbor_ids:
            # Neighbor has parent: neighbor is part of an original island.
            if neighbor_id in self.parents.keys():
                parent_id = self.parents[neighbor_id]
                if parent_id not in visited_parent_ids:
                    island_size += self.island_sizes[parent_id]  # Combine neighbor islands.
                    visited_parent_ids.add(parent_id)  # Prevent adding duplicates.

        if island_size > self.largest_island:
            self.largest_island = island_size
