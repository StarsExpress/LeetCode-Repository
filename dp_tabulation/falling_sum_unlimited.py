
def _binary_sort(target: tuple[int, int], sorted_val_idx: list[tuple[int, int]]) -> int:
    if len(sorted_val_idx) <= 0:
        return 0

    back_idx, front_idx = 0, len(sorted_val_idx) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_val_idx[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of tuples < target, implying insertion idx.


def find_unlimited_falling_sum(grid: list[list[int]]) -> int:  # LeetCode Q.1289.
    if len(grid) == 1:  # Base case: matrix has just one row.
        return min(grid[0])

    path_sum = []  # Track cumulated path sum until each entry.
    for idx, row in enumerate(grid):
        if idx == 0:  # Base case: matrix's top row.
            path_sum.append(grid[0])
            continue
        path_sum.append([0] * len(row))

    last_row_mins = []  # Last row's two (if exist) min sums & indices.
    current_row_mins = []  # Current row's two (if exist) min sums & indices.

    for row_idx, row in enumerate(grid):
        for entry_idx, entry in enumerate(row):
            if row_idx != 0:  # 1st row's path sum is already finished base case.
                path_sum[row_idx][entry_idx] += entry  # Self value from matrix.

                # Min cumulated sum of different idx from upper row.
                if entry_idx == last_row_mins[0][1]:
                    path_sum[row_idx][entry_idx] += last_row_mins[1][0]

                else:
                    path_sum[row_idx][entry_idx] += last_row_mins[0][0]

            # Update each row's two (if exist) mins.
            insertion_idx = _binary_sort(
                (path_sum[row_idx][entry_idx], entry_idx), current_row_mins
            )
            if insertion_idx < 2:  # Only need two min.
                current_row_mins.insert(
                    insertion_idx, (path_sum[row_idx][entry_idx], entry_idx)
                )
            if len(current_row_mins) > 2:  # Only need two min.
                current_row_mins.pop(-1)

        last_row_mins.clear()  # Update & reset for next iteration.
        last_row_mins.extend(current_row_mins)
        current_row_mins.clear()

    return min(path_sum[-1])
