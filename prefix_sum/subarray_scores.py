
def count_subarray_scores(integers: list[int], target: int):  # LeetCode Q.2302.
    """
    Count number of subarrays whose sum is strictly less than target.
    Key: integers are all positive, making prefix sums monotonically increasing.
    """
    prefix_sums = []
    for integer in integers:
        if not prefix_sums:  # 1st int.
            prefix_sums.append(integer)
            continue
        prefix_sums.append(prefix_sums[-1] + integer)

    count, queue = 0, []  # (Prefix sum end idx) increasing monotonic queue.
    for end_idx, prefix_sum in enumerate(prefix_sums):
        # Subarrays from (queue[0] + 1)th idx to (end_idx)th idx.
        # If a start idx & current end idx exceed target, so will a bigger end idx with this start idx.
        while queue and (prefix_sum - prefix_sums[queue[0]]) * (end_idx - queue[0]) >= target:
            queue.pop(0)

        count += len(queue)

        if prefix_sum * (end_idx + 1) < target:  # Subarray from 0th idx to (end_idx)th idx.
            count += 1

        queue.append(end_idx)

    return count
