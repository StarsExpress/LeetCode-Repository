
class RangeSum:  # LeetCode Q.307.
    """Update values and query range sum."""

    def __init__(self, integers: list[int]):
        self.integers, self.total_ints = integers, len(integers)
        self.tree = [0] * 2 * self.total_ints
        self.build_tree()

    def build_tree(self):
        for i in range(self.total_ints):  # Leaf nodes.
            self.tree[self.total_ints + i] += self.integers[i]

        for i in range(self.total_ints - 1, 0, -1):  # Parent nodes.
            self.tree[i] += self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, value: int):
        index += self.total_ints
        self.tree[index] = value
        while index > 1:    # Move upward to update parents.
            self.tree[index >> 1] = self.tree[index] + self.tree[index ^ 1]
            index >>= 1

    def find_range_sum(self, left_idx: int, right_idx: int):
        left_idx += self.total_ints
        right_idx += self.total_ints + 1  # Right idx is required to be "inclusive".
        range_sum = 0

        while left_idx < right_idx:
            if left_idx & 1:
                range_sum += self.tree[left_idx]
                left_idx += 1

            if right_idx & 1:
                right_idx -= 1
                range_sum += self.tree[right_idx]

            left_idx >>= 1
            right_idx >>= 1

        return range_sum
