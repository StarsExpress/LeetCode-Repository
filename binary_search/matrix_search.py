
def _binary_search(target: int | list[int], sorted_list: list[int] | list[list[int]], size: int):
    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_list[mid_idx] == target:
            return True, mid_idx

        if sorted_list[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return False, back_idx  # Back idx implies number of items < target.


def search_over_matrix(matrix: list[list[int]], target: int):  # LeetCode Q.74.
    total_rows, total_cols = len(matrix), len(matrix[0])
    _, row_idx = _binary_search([target], matrix, total_rows)
    if row_idx == 0:
        return _binary_search(target, matrix[0], total_cols)[0]

    # Row idx isn't 0: target in (row_idx - 1)th or (row_idx)th rows.
    if _binary_search(target, matrix[row_idx - 1], total_cols)[0]:
        return True

    if row_idx == total_rows:  # "The next row" doesn't exist.
        return False
    return _binary_search(target, matrix[row_idx], total_cols)[0]
