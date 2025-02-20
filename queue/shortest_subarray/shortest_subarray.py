
def find_shortest_subarray_length(nums: list[int], target: int) -> int:  # LeetCode Q.862.
    """Find the shortest subarray length with sum >= target."""
    prefix_sum, min_len = 0, float("inf")

    # Prefix sum increasing monotonic queue.
    queue: list[tuple[int, int]] = []  # Format: (prefix sum, subarray len).

    for idx, num in enumerate(nums):
        if num >= target:  # Base case.
            return 1

        prefix_sum += num
        if prefix_sum >= target and idx + 1 < min_len:
            min_len = idx + 1  # Subarray from 0th to (idx)th idx.

        # Subarrays from (queue[0][1] + 1)th idx to (idx)th idx.
        while queue and prefix_sum - queue[0][0] >= target:
            if idx + 1 - queue[0][1] < min_len:
                min_len = idx + 1 - queue[0][1]
            # Later subarrays can't reset record with this past subarray.
            queue.pop(0)

        # Increase probability of meeting k with shorter subarrays.
        while queue and prefix_sum < queue[-1][0]:
            queue.pop(-1)  # Make queue's prefix sums smaller if possible.

        queue.append((prefix_sum, idx + 1))

    return -1 if min_len == float("inf") else min_len
