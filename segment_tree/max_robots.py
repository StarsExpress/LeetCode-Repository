
class SegmentTree:
    def __init__(self, data: list[int] | tuple[int]):
        self.length = len(data)
        self.tree = [0] * (2 * self.length)
        self._build(data)

    def _build(self, data: list[int] | tuple[int]):
        for i in range(self.length):
            self.tree[self.length + i] = data[i]

        for i in range(self.length - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def find_range_max(self, left_idx: int, right_idx: int):
        # Get max value in interval [left_idx, right_idx).
        range_max = float('-inf')

        left_idx += self.length
        right_idx += self.length
        while left_idx < right_idx:
            if left_idx % 2 == 1:
                range_max = max(range_max, self.tree[left_idx])
                left_idx += 1

            if right_idx % 2 == 1:
                right_idx -= 1
                range_max = max(range_max, self.tree[right_idx])

            left_idx //= 2
            right_idx //= 2

        return range_max


def count_max_robots(charge_times: list[int], running_costs: list[int], budget: int):  # LeetCode Q.2398.
    # Base case: only 1st robot.
    max_len = 1 if budget >= charge_times[0] + running_costs[0] else 0
    if len(charge_times) == len(running_costs) == 1:
        return max_len

    cost_prefix_sums = []
    for cost in running_costs:
        if not cost_prefix_sums:  # 1st cost.
            cost_prefix_sums.append(cost)
            continue
        cost_prefix_sums.append(cost_prefix_sums[-1] + cost)

    segment_tree = SegmentTree(charge_times)

    queue = []  # (Cost prefix sum end idx) increasing monotonic queue.
    for end_idx, prefix_sum in enumerate(cost_prefix_sums):
        while queue:
            # Subarrays from (queue[0] + 1)th idx to (end_idx)th idx.
            subarray_max = segment_tree.find_range_max(queue[0] + 1, end_idx + 1)
            if subarray_max + (end_idx - queue[0]) * (prefix_sum - cost_prefix_sums[queue[0]]) <= budget:
                break

            # If a start idx & current end idx exceed budget, so will a bigger end idx with this start idx.
            queue.pop(0)

        if queue:
            if end_idx - queue[0] > max_len:  # Check the longest subarray in queue.
                max_len = end_idx - queue[0]

            if queue[0] == 0:  # Also check subarray from 0th idx to (end_idx)th idx.
                subarray_max = max(charge_times[queue[0]], charge_times[0])
                if subarray_max + (end_idx + 1) * prefix_sum <= budget:
                    max_len = end_idx + 1

        queue.append(end_idx)

    return max_len
