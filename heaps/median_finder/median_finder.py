import heapq


class MedianFinder:  # LeetCode Q.295.
    """Find median inside stream."""
    def __init__(self):
        self.min_heap, self.min_heap_len = [], 0
        self.max_heap, self.max_heap_len = [], 0
        self.latest_median = None

    def add_num(self, num: int):
        if self.latest_median is None:
            heapq.heappush(self.min_heap, num)
            self.min_heap_len += 1
            self.latest_median = num
            return

        if num < self.latest_median:
            heapq.heappush(self.max_heap, -num)  # Minus sign for max heap.
            self.max_heap_len += 1

        else:
            heapq.heappush(self.min_heap, num)
            self.min_heap_len += 1

        if self.max_heap_len - 1 > self.min_heap_len:  # Ensure heaps size diff <= 1.
            max_heap_root = -heapq.heappop(self.max_heap)  # Minus sign for max heap.
            self.max_heap_len -= 1

            heapq.heappush(self.min_heap, max_heap_root)
            self.min_heap_len += 1

        if self.min_heap_len - 1 > self.max_heap_len:  # Ensure heaps size diff <= 1.
            min_heap_root = heapq.heappop(self.min_heap)
            self.min_heap_len -= 1

            heapq.heappush(self.max_heap, -min_heap_root)  # Minus sign for max heap.
            self.max_heap_len += 1

        if self.min_heap_len == self.max_heap_len:  # Minus sign for max heap.
            self.latest_median = (self.min_heap[0] - self.max_heap[0]) / 2

        if self.min_heap_len > self.max_heap_len:
            self.latest_median = self.min_heap[0]

        if self.min_heap_len < self.max_heap_len:
            self.latest_median = -self.max_heap[0]  # Minus sign for max heap.

    def find_median(self):
        return self.latest_median
