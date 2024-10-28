
def find_min_path_sum(triangle: list[list[int]]) -> int:  # LeetCode Q.120.
    """
    Given a triangle array, return minimum path sum from top to bottom.
    For each step, you may move to an adjacent number of the row below.
    If you are on index i on current row, you may move to either index i or i + 1 on next row.
    """
    path_sum = [[0] * len(row) for row in triangle]  # Track cumulated path sum until each entry.
    path_sum[0][0] += triangle[0][0]  # Base case: triangle's top.

    for row_idx, row in enumerate(triangle):
        if row_idx == 0:  # Base case is already finished.
            continue

        for entry_idx, entry in enumerate(row):  # First take self value from triangle.
            path_sum[row_idx][entry_idx] += triangle[row_idx][entry_idx]

            # Take min cumulated path sum from upper row.
            if entry_idx - 1 < 0:  # Must take upper right.
                path_sum[row_idx][entry_idx] += path_sum[row_idx - 1][entry_idx]
                continue

            if entry_idx >= len(path_sum[row_idx - 1]):  # Must take upper left.
                path_sum[row_idx][entry_idx] += path_sum[row_idx - 1][entry_idx - 1]
                continue

            # Both upper right & left exist: take min.
            path_sum[row_idx][entry_idx] += min(
                path_sum[row_idx - 1][entry_idx], path_sum[row_idx - 1][entry_idx - 1]
            )

    return min(path_sum[-1])
