
def find_min_path_sum(grid: list[list[int]]) -> int:  # LeetCode Q.64.
    rows, cols = len(grid), len(grid[0])
    paths_sum = [[0] * cols for _ in range(rows)]
    paths_sum[0][0] = grid[0][0]  # Base case: triangle's top-left.

    for j in range(1, cols):
        paths_sum[0][j] += paths_sum[0][j - 1] + grid[0][j]

    for i in range(1, rows):
        paths_sum[i][0] += paths_sum[i - 1][0] + grid[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            paths_sum[i][j] += min(paths_sum[i - 1][j], paths_sum[i][j - 1]) + grid[i][j]

    return paths_sum[-1][-1]
