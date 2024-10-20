
class DinnerPlates:  # LeetCode Q.1172.
    def __init__(self, capacity: int):
        self.stacks, self.total_stacks = [], 0
        self.capacity = capacity
        self.leftmost_openings, self.total_openings = [], 0

    def push(self, value: int) -> None:
        if not self.leftmost_openings:  # Go to rightmost stack.
            if self.stacks and len(self.stacks[-1]) < self.capacity:
                self.stacks[-1].insert(0, value)
                return

            self.stacks.append([value])  # Open another stack.
            self.total_stacks += 1
            return

        stack_idx = self.leftmost_openings.pop(0)  # Go to leftmost open stack.
        self.stacks[stack_idx].insert(0, value)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        if not self.stacks[-1]:
            return -1

        plate = self.stacks[-1].pop(0)  # Take the plate on top.

        while self.stacks and not self.stacks[-1]:  # Empty rightmost stack.
            # Ensure leftmost openings don't contain "empty" rightmost stack.
            while self.leftmost_openings:
                if self.leftmost_openings[-1] != self.total_stacks - 1:
                    break
                self.leftmost_openings.pop(-1)

            self.stacks.pop(-1)
            self.total_stacks -= 1

        if self.total_stacks <= 1:  # Leftmost openings only exist when num of stacks >= 2.
            self.leftmost_openings.clear()

        return plate

    def pop_specific_stack(self, index: int) -> int:
        if not self.stacks or index >= self.total_stacks:
            return -1
        if not self.stacks[index]:
            return -1

        if index == self.total_stacks - 1:  # Equivalent to pop method.
            return self.pop()

        insertion_idx = self._binary_search(index)
        self.leftmost_openings.insert(insertion_idx, index)
        return self.stacks[index].pop(0)  # Take the plate on top.

    def _binary_search(self, index: int):
        if self.total_openings == 0:
            return 0

        back_idx, front_idx = 0, self.total_openings - 1
        while back_idx <= front_idx:
            mid_idx = (back_idx + front_idx) // 2
            if self.leftmost_openings[mid_idx] < index:
                back_idx = mid_idx + 1
                continue
            front_idx = mid_idx - 1

        return back_idx  # Number of indices < target idx.
