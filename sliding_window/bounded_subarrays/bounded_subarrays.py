
def count_bounded_subarrays(nums: list[int], minimum: int, maximum: int):  # LeetCode Q.2444.
    bounded_subarrays = 0
    left_bound = 0  # Min start idx of fixed subarrays ending at current idx.
    min_prev_idx, max_prev_idx = -1, -1  # Latest indices of min k and max k.
    for idx, num in enumerate(nums):
        if num < minimum or maximum < num:  # Current num is out of bounds.
            min_prev_idx, max_prev_idx = -1, -1  # Reset indices.
            left_bound = idx + 1  # Reset left bound.
            continue

        if num == minimum:
            min_prev_idx = idx
        if num == maximum:
            max_prev_idx = idx

        # Current num is the end of bounded subarrays.
        if min(min_prev_idx, max_prev_idx) != -1:
            # Max start idx = the smaller of min prev idx and max prev idx.
            bounded_subarrays += min(min_prev_idx, max_prev_idx) + 1 - left_bound

    return bounded_subarrays
