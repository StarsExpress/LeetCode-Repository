
class MedianFinder:  # LeetCode Q.295.
    """Find median inside stream."""
    def __init__(self):
        self.nums, self.len = [], 0  # Track length of nums list.

    def add_num(self, num: int):
        insertion_idx = self._binary_search(num)
        self.nums.insert(insertion_idx, num)
        self.len += 1

    def find_median(self):
        if self.len % 2 == 0:
            return (self.nums[(self.len // 2) - 1] + self.nums[self.len // 2]) / 2
        return self.nums[self.len // 2]

    def _binary_search(self, target: int):
        if not self.nums:
            return 0

        back_idx, front_idx = 0, len(self.nums) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.nums[mid_idx] < target:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of ints < target int.
