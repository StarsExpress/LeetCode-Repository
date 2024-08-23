
def find_shortest_subarray(integers: list[int], target: int):  # LeetCode Q.862.
    """Find the shortest subarray with sum >= target."""
    prefix_sum, min_len = 0, float("inf")
    queue = []  # Prefix sum end idx increasing monotonic queue.
    for idx, integer in enumerate(integers):
        if integer >= target:  # Base case.
            return 1

        if idx == 0:  # 1st int.
            prefix_sum += integer
            queue.append((prefix_sum, 0))  # Format: (prefix sum, its ending idx).
            continue

        prefix_sum += integer  # Update prefix sum ending at idx.

        # Subarrays from (queue[0][1] + 1)th idx to (idx)th idx.
        while queue and prefix_sum - queue[0][0] >= target:
            if idx - queue[0][1] < min_len:
                min_len = idx - queue[0][1]
            queue.pop(0)

        if prefix_sum >= target and idx + 1 < min_len:  # Subarray from 0th idx to (idx)th idx.
            min_len = idx + 1

        # Make queue's prefix sums smaller as bigger subarray sum is preferred.
        while queue and prefix_sum < queue[-1][0]:
            queue.pop(-1)

        queue.append((prefix_sum, idx))  # Format: (prefix sum, its ending idx).

    return min_len if min_len != float("inf") else -1
