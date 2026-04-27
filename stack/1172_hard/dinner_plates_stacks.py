import heapq


class DinnerPlatesStacks:  # LeetCode Q.1172.
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.plates_stacks: list[list[int]] = []

        # Min heap of indices of stacks that aren't full yet.
        self.free_stacks_heap: list[int] = []

    def push(self, plate: int) -> None:
        if self.free_stacks_heap:
            free_stack_idx = self.free_stacks_heap[0]
            if free_stack_idx < len(self.plates_stacks):
                self.plates_stacks[free_stack_idx].append(plate)
                if len(self.plates_stacks[free_stack_idx]) == self.max_capacity:
                    heapq.heappop(self.free_stacks_heap)
                return

            self.free_stacks_heap.clear()  # Reset: all free stacks exist no more.

        if not self.plates_stacks:  # No stacks at all.
            self.plates_stacks.append([])

        if len(self.plates_stacks[-1]) == self.max_capacity:  # Full rightmost stack.
            self.plates_stacks.append([])

        self.plates_stacks[-1].append(plate)

    def pop(self) -> int:
        if not self.plates_stacks:
            return -1

        plate = self.plates_stacks[-1].pop(-1)
        while self.plates_stacks and not self.plates_stacks[-1]:
            self.plates_stacks.pop(-1)  # Drop empty rightmost stacks.

        return plate

    def pop_specific_stack(self, index: int) -> int:
        if index >= len(self.plates_stacks):
            return -1

        if not self.plates_stacks[index]:
            return -1

        if index == len(self.plates_stacks) - 1:
            return self.pop()

        # Becomes not full after this pop: enter heap.
        if len(self.plates_stacks[index]) == self.max_capacity:
            heapq.heappush(self.free_stacks_heap, index)

        return self.plates_stacks[index].pop(-1)
