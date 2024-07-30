
def find_shortest_subarray(integers: list[int], target: int):  # LeetCode Q.862.
    """Find the shortest subarray with sum >= target."""
    prefix_sums = []
    for integer in integers:
        if integer >= target:  # Answer of 1 directly found.
            return 1

        if len(prefix_sums) <= 0:  # 1st int.
            prefix_sums.append(integer)
            continue
        prefix_sums.append(prefix_sums[-1] + integer)

    min_len, queue = float("inf"), []  # (Prefix sum end idx) increasing monotonic queue.
    for end_idx, prefix_sum in enumerate(prefix_sums):
        # Subarrays from (queue[0] + 1)th idx to (end_idx)th idx.
        while queue and prefix_sum - prefix_sums[queue[0]] >= target:
            current_len = end_idx - queue.pop(0)
            if current_len < min_len:
                min_len = current_len

        # Subarray from 0th idx to (end_idx)th idx.
        if prefix_sum >= target and end_idx + 1 < min_len:
            min_len = end_idx + 1

        # Make queue's stored prefix sums smaller as bigger subarray sum is preferred.
        while queue and prefix_sum < prefix_sums[queue[-1]]:
            queue.pop(-1)

        queue.append(end_idx)

    return min_len if min_len != float("inf") else -1
