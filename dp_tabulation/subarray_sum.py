
def compute_max_subarray_sum(integers: list[int]) -> int:  # LeetCode Q.53.
    subarray_sum = integers.pop(0)
    max_sum = subarray_sum  # Base case.

    for integer in integers:
        if subarray_sum < 0:  # Negative sum: reset subarray.
            subarray_sum = 0

        subarray_sum += integer
        if subarray_sum > max_sum:
            max_sum = subarray_sum

    return max_sum
