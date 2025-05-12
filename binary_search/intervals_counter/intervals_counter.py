from bisect import bisect_right


class IntervalsCounter:  # LeetCode Q.2276.
    def __init__(self):
        self.ranges = []  # Format: [inclusive left, inclusive right].
        self.covered_nums = 0

    def add(self, left: int, right: int) -> None:
        idx = bisect_right(self.ranges, [left, right])

        if idx > 0 and self.ranges[idx - 1][1] + 1 >= left:  # Merge prev range.
            idx -= 1  # Insertion idx changes.
            self.covered_nums -= self.ranges[idx][1] + 1 - self.ranges[idx][0]
            right = max(right, self.ranges[idx][1])
            self.ranges[idx][1] = right
            left = self.ranges[idx][0]

        else:
            self.ranges.insert(idx, [left, right])

        while idx + 1 < len(self.ranges) and self.ranges[idx + 1][0] - 1 <= right:
            self.covered_nums -= self.ranges[idx + 1][1] + 1 - self.ranges[idx + 1][0]
            right = max(right, self.ranges[idx + 1][1])
            self.ranges[idx][1] = right
            self.ranges.pop(idx + 1)  # Next range is merged.

        self.covered_nums += right + 1 - left

    def count(self) -> int:
        return self.covered_nums
