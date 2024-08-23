
def count_subarray_scores(integers: list[int], target: int):  # LeetCode Q.2302.
    """
    Count number of subarrays whose sum is strictly less than target.

    Key: integers are all positive, making prefix sums monotonically increasing.
    If subarray from start idx + 1 to idx can't stay under target,
    so can't a bigger idx with this start idx.
    """
    count, start_idx = 0, 0  # Min possible start idx to stay under target with current idx.
    prefix_sums = []
    for idx, integer in enumerate(integers):
        if not prefix_sums:  # 1st int.
            prefix_sums.append(integer)
            if integer < target:
                count += 1
            continue

        prefix_sums.append(prefix_sums[-1] + integer)  # Update prefix sum at idx.

        # Subarrays from (start_idx + 1)th idx to (idx)th idx.
        while (prefix_sums[-1] - prefix_sums[start_idx]) * (idx - start_idx) >= target:
            start_idx += 1
        count += idx - start_idx

        if prefix_sums[-1] * (idx + 1) < target:  # Subarray from 0th idx to (idx)th idx.
            count += 1

    return count
