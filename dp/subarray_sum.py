
def compute_max_subarray_sum(integers: list[int]):  # LeetCode Q.53.
    subarray_sum = integers.pop(0)
    max_sum = subarray_sum  # Base case.

    while integers:
        if subarray_sum < 0:  # Negative subarray sum: new number should "reset" subarray before joining it.
            subarray_sum = 0
        subarray_sum += integers.pop(0)  # Non-negative subarray sum: new number directly joins it.
        if subarray_sum > max_sum:
            max_sum = subarray_sum

    return max_sum
