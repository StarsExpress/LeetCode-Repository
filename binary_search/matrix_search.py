
def binary_search(target: int, sorted_integers: list[int] | tuple[int]):
    if len(sorted_integers) <= 0:
        return False, 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while True:
        if back_idx > front_idx:
            return False, back_idx

        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] == target:
            return True, mid_idx

        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def search_over_matrix(matrix: list[list[int]], target: int):  # LeetCode Q.74.
    rows_heads = [matrix[i][0] for i in range(len(matrix))]
    found, row_idx = binary_search(target, rows_heads)
    return True if found else binary_search(target, matrix[row_idx - 1])[0]
