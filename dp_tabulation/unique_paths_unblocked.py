
def count_unique_unblocked_paths(obstacles_grid: list[list[int]]) -> int:  # LeetCode Q.63.
    if obstacles_grid[0][0] == 1:  # Base case: if start point is already blocked.
        return 0

    rows, columns = len(obstacles_grid), len(obstacles_grid[0])

    unblocked_1st_row_count = rows  # Find out unblocked counts in 1st row.
    for row_idx, row_entries in enumerate(obstacles_grid):
        if row_entries[0] == 1:  # This entry's right row entries are all blocked.
            unblocked_1st_row_count = row_idx
            break

    unblocked_1st_col_count = columns  # Find out unblocked counts in 1st column.
    if 1 in obstacles_grid[0]:  # This entry's lower column entries are all blocked.
        unblocked_1st_col_count = obstacles_grid[0].index(1)

    unique_paths = []
    for row_idx in range(rows):
        if row_idx == 0:  # Base case: fill in 1st row and 1st column entries.
            unique_paths.append(
                [1] * unblocked_1st_col_count + [0] * (columns - unblocked_1st_col_count)
            )
            continue

        if row_idx >= unblocked_1st_row_count:  # Non-1st row entirely blocked.
            unique_paths.append([0] * columns)
            continue

        unique_paths.append([1] + [0] * (columns - 1))

    for row_idx in range(1, rows):  # State transition: [i][j] is visited by [i - 1][j] & [i][j - 1].
        for col_idx in range(1, columns):
            if obstacles_grid[row_idx][col_idx] != 1:  # Only update unblocked spots.
                unique_paths[row_idx][col_idx] += unique_paths[row_idx - 1][col_idx]
                unique_paths[row_idx][col_idx] += unique_paths[row_idx][col_idx - 1]

    return unique_paths[-1][-1]
