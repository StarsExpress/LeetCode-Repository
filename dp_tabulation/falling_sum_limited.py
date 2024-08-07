
def find_limited_falling_sum(matrix: list[list[int]]):  # LeetCode Q.931.
    path_sum = []  # Track cumulated path sum until each entry.
    for idx, row in enumerate(matrix):
        if idx == 0:  # Base case: matrix's top row.
            path_sum.append(matrix[0])
            continue
        path_sum.append([0] * len(row))

    for row_idx, row in enumerate(matrix):
        if row_idx == 0:  # Base case is already finished.
            continue

        for entry_idx, entry in enumerate(row):  # First take self value from matrix.
            path_sum[row_idx][entry_idx] += entry

            # Take min cumulated path sum from upper row. Beware of left & right end indices.
            left_upper_sum = path_sum[row_idx - 1][max(0, entry_idx - 1)]
            mid_upper_sum = path_sum[row_idx - 1][entry_idx]
            right_upper_sum = path_sum[row_idx - 1][min(len(row) - 1, entry_idx + 1)]
            path_sum[row_idx][entry_idx] += min(left_upper_sum, mid_upper_sum, right_upper_sum)

    return min(path_sum[-1])
