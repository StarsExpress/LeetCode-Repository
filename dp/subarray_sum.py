
def compute_max_subarray_sum(integers: list[int]):  # LeetCode Q.53.
    subarray_sum = integers.pop(0)
    max_sum = subarray_sum  # Base case.

    while len(integers) >= 0:
        if subarray_sum > max_sum:
            max_sum = subarray_sum

        if len(integers) == 0:
            return max_sum

        if subarray_sum < 0:  # Negative subarray sum: new int should "reset" subarray before joining it.
            subarray_sum = 0
        subarray_sum += integers.pop(0)  # Non-negative subarray sum: new int directly joins it.
