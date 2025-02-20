
def discover_valid_path(grid: list[list[str]]) -> bool:  # LeetCode Q.2267.
    last_row: list[set[int]] = []
    current_row: list[set[int]] = []
    total_rows, total_cols = len(grid), len(grid[0])
    for row_idx in range(total_rows):
        # Remaining path length after inclusion of current spot.
        remaining_len = total_rows + total_cols - 2 - row_idx
        dead_row = True  # Default to dead row: current row is entirely blocked.

        for col_idx in range(total_cols):
            current_row.append(set())
            diff = 1 if grid[row_idx][col_idx] == "(" else -1

            # Valid paths' prefix: left parentheses count >= right parentheses count.
            # Remaining path length must >= current diff of parentheses.
            if row_idx == col_idx == 0 and 0 <= diff <= remaining_len:
                current_row[0].add(diff)

            if row_idx > 0:
                for cumulated_diff in last_row[col_idx]:
                    cumulated_diff += diff
                    if 0 <= cumulated_diff <= remaining_len:
                        current_row[col_idx].add(cumulated_diff)

            if col_idx > 0:
                for cumulated_diff in current_row[col_idx - 1]:
                    cumulated_diff += diff
                    if 0 <= cumulated_diff <= remaining_len:
                        current_row[col_idx].add(cumulated_diff)

            if current_row[col_idx] and dead_row:  # Current row won't be dead.
                dead_row = False

            remaining_len -= 1  # Update for the right neighbor in the same row.

        if dead_row:
            return False

        last_row[:] = current_row[:]  # Must use [:] to update list of sets.
        current_row.clear()  # Reset for the next row.

    return 0 in last_row[-1]
