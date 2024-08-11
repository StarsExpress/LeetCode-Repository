
class DinnerPlates:  # LeetCode Q.1172.
    def __init__(self, capacity: int):
        self.stacks, self.capacity = [], capacity
        self.left_side_openings = []

    def push(self, val: int):
        if not self.left_side_openings:  # Go to rightmost stack.
            if self.stacks and len(self.stacks[-1]) < self.capacity:
                self.stacks[-1].insert(0, val)
                return

            self.stacks.append([val])  # Open another stack.
            return

        stack_idx = self.left_side_openings.pop(0)  # Go to left side open stack.
        self.stacks[stack_idx].insert(0, val)

    def pop(self):
        if not self.stacks:
            return -1
        if not self.stacks[-1]:
            return -1

        plate = self.stacks[-1].pop(0)  # Take the plate on top.

        while self.stacks and not self.stacks[-1]:  # Empty rightmost stack.
            # Ensure left side openings don't contain "empty" rightmost stack.
            while self.left_side_openings:
                if self.left_side_openings[-1] != len(self.stacks) - 1:
                    break
                self.left_side_openings.pop(-1)

            self.stacks.pop(-1)

        if len(self.stacks) <= 1:  # Left side openings only exist when num of stacks >= 2.
            self.left_side_openings.clear()

        return plate

    def pop_specific_stack(self, index: int):
        if not self.stacks or index >= len(self.stacks):
            return -1
        if not self.stacks[index]:
            return -1

        if index == len(self.stacks) - 1:  # Equivalent to pop method.
            return self.pop()

        insertion_idx = self._binary_search(index)
        self.left_side_openings.insert(insertion_idx, index)
        return self.stacks[index].pop(0)  # Take the plate on top.

    def _binary_search(self, index: int):
        if not self.left_side_openings:
            return 0

        back_idx, front_idx = 0, len(self.left_side_openings) - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.left_side_openings[mid_idx] < index:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of indices < target idx.
