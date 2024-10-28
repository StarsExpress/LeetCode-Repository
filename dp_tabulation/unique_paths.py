
def count_unique_paths(rows: int, columns: int) -> int:  # LeetCode Q.62.
    """
    There is a robot on an m x n grid. Robot is initially located at top-left corner.
    Robot tries to move to bottom-right corner.
    Robot can only move either down or right at any point in time.
    """
    unique_paths = []
    for row_idx in range(rows):  # Base case: 1st row and 1st column are all with entries 1.
        if row_idx == 0:
            unique_paths.append([1] * columns)
            continue
        unique_paths.append([1] + [0] * (columns - 1))

    for row_idx in range(1, rows):  # State transition: [i][j] is visited by [i - 1][j] & [i][j - 1].
        for col_idx in range(1, columns):
            unique_paths[row_idx][col_idx] += unique_paths[row_idx - 1][col_idx] + unique_paths[row_idx][col_idx - 1]
    return unique_paths[-1][-1]
