
def find_max_distance(sorted_arrays: list[list[int]]) -> int:  # LeetCode Q.624.
    max_dist = 0
    min_int, max_int = float("inf"), -float("inf")  # Min & max values of all arrays.
    for sorted_array in sorted_arrays:
        has_min, has_max = False, False  # If current array has min & max values.
        if sorted_array[0] < min_int:
            has_min = True
        if sorted_array[-1] > max_int:
            has_max = True

        if not has_min and not has_max:
            max_dist = max(max_int - sorted_array[0], sorted_array[-1] - min_int, max_dist)
            continue

        if has_min and has_max:
            if sorted_array[-1] - min_int > max_dist:
                max_dist = sorted_array[-1] - min_int

            if max_int - sorted_array[0] > max_dist:
                max_dist = max_int - sorted_array[0]

            min_int, max_int = sorted_array[0], sorted_array[-1]
            continue

        if has_min:
            min_int = sorted_array[0]
        if has_max:
            max_int = sorted_array[-1]

        if max_int - min_int > max_dist:
            max_dist = max_int - min_int

    return max_dist
