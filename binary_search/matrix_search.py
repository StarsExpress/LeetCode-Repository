
def binary_search(target, sorted_list: list):
    if len(sorted_list) <= 0:
        return False, 0

    back_idx, front_idx = 0, len(sorted_list) - 1
    while True:
        if back_idx > front_idx:
            return False, back_idx  # Back idx implies number of items < target.

        mid_idx = (back_idx + front_idx) // 2
        if sorted_list[mid_idx] == target:
            return True, mid_idx

        if sorted_list[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def search_over_matrix(matrix: list[list[int]], target: int):  # LeetCode Q.74.
    _, row_idx = binary_search([target], matrix)
    if row_idx == 0:
        return binary_search(target, matrix[0])[0]
    if binary_search(target, matrix[row_idx - 1])[0]:  # Target may be in (row_idx - 1)th or (row_idx)th rows.
        return True
    # If row idx = last matrix row, "the next row" doesn't exist.
    return False if row_idx == len(matrix) else binary_search(target, matrix[row_idx])[0]
