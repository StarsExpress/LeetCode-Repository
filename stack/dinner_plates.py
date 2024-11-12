import heapq


class DinnerPlates:  # LeetCode Q.1172.
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.stacks, self.total_stacks = [], 0
        self.queue, self.queue_len = [], 0

    def push(self, value: int) -> None:
        while self.queue and self.queue[0] >= self.total_stacks:
            heapq.heappop(self.queue)
            self.queue_len -= 1

        while self.queue_len >= 2 and self.queue[0] == self.queue[1]:
            heapq.heappop(self.queue)
            self.queue_len -= 1

        if not self.queue:  # Open another stack.
            self.stacks.append([value])
            self.total_stacks += 1

            if self.capacity > 1:
                heapq.heappush(self.queue, self.total_stacks - 1)
                self.queue_len += 1
            return

        stack_idx = self.queue[0]  # Leftmost open stack.
        self.stacks[stack_idx].append(value)
        if len(self.stacks[stack_idx]) >= self.capacity:
            heapq.heappop(self.queue)
            self.queue_len -= 1

    def pop(self) -> int:
        if not self.stacks or not self.stacks[-1]:
            return -1

        plate = self.stacks[-1].pop(-1)  # Take the plate on top.
        if len(self.stacks[-1]) + 1 == self.capacity:  # Not in queue and must join it now.
            heapq.heappush(self.queue, self.total_stacks - 1)
            self.queue_len += 1

        while self.stacks and not self.stacks[-1]:  # Empty rightmost stack.
            self.stacks.pop(-1)
            self.total_stacks -= 1

        if self.total_stacks == 0:
            self.queue.clear()
            self.queue_len -= self.queue_len

        return plate

    def pop_specific_stack(self, index: int) -> int:
        if not self.stacks or index >= self.total_stacks:
            return -1
        if not self.stacks[index]:
            return -1

        if index == self.total_stacks - 1:  # Equivalent to pop method.
            return self.pop()

        heapq.heappush(self.queue, index)
        self.queue_len += 1
        return self.stacks[index].pop(-1)  # Take the plate on top.
