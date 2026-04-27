import heapq


def kth_smallest_rows_sum(matrix: list[list[int]], k: int) -> int:  # LeetCode Q.1439.
    """Matrix's each row must be sorted in non-decreasing order. k <= columns ** rows."""
    total_rows, total_cols = len(matrix), len(matrix[0])

    min_heap = [  # (Rows sum, each row's selected column idx in str format).
        (sum(row[0] for row in matrix), ["0"] * total_rows)
    ]
    k_min_sum = 0
    visited_combos = {":".join(min_heap[0][1])}  # Combos of each row's col idx.

    while 0 < k:
        rows_sum, col_indices = heapq.heappop(min_heap)
        k -= 1
        if k == 0:
            k_min_sum += rows_sum
            break

        for row_idx in range(total_rows):
            col_idx = int(col_indices[row_idx])
            if col_idx + 1 < total_cols:  # Can move 1 spot in iterated row.
                col_indices[row_idx] = str(col_idx + 1)
                combo = ":".join(col_indices)
                if combo not in visited_combos:  # Current indices combo is unused.
                    new_rows_sum = rows_sum - matrix[row_idx][col_idx] + matrix[row_idx][col_idx + 1]
                    # Use copy to reflect updated str col indices.
                    heapq.heappush(min_heap, (new_rows_sum, col_indices.copy()))
                    visited_combos.add(combo)

                col_indices[row_idx] = str(col_idx)  # Revert to previous value.

    return k_min_sum
