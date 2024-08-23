
def count_sum(numbers: list[int], goal: int):  # LeetCode Q.930.
    queue = []  # Prefix sum increasing monotonic queue.
    count, prefix_sum = 0, 0
    for idx, num in enumerate(numbers):
        if idx == 0:  # 1st int.
            prefix_sum += num
            queue.append([num, 1])  # Format: (prefix sum, occurrences of such sum).
            if num == goal:
                count += 1
            continue

        prefix_sum += num

        while queue and prefix_sum - queue[0][0] > goal:
            queue.pop(0)

        # Subarrays from some non-0th indices to (idx)th idx.
        if queue and prefix_sum - queue[0][0] == goal:
            count += queue[0][1]

        if prefix_sum == goal:  # Subarray from 0th idx to (idx)th idx.
            count += 1

        if queue and queue[-1][0] == prefix_sum:
            queue[-1][1] += 1  # Increment occurrences.
            continue

        queue.append([prefix_sum, 1])  # Format: (prefix sum, occurrences of such sum).

    return count
