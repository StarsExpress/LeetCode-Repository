import math
from copy import deepcopy


class MinHeap:
    """Apply min heap to sort items."""

    def __init__(self, items: list | tuple):
        self.items_list = []
        self.items_list.extend(items)

    def build_heap(self):  # Ensure the min item is at root before any "non-recursive" heapify calls.
        total_subtrees = math.floor(len(self.items_list) / 2)
        for i in reversed(range(total_subtrees)):
            self.heapify(root_idx=i)

    def add_items(self, items, reset=False):
        if isinstance(items, dict):
            return

        if reset:
            self.items_list.clear()

        if isinstance(items, list) | isinstance(items, tuple):
            self.items_list.extend(items)

        else:
            self.items_list.append(items)
        self.build_heap()  # Ensure the min item is still at root.

    def heapify(self, root_idx: int = 0):  # Subtree's root index has default of uppermost subtree's index.
        # Root index at ith: left child index at 2i + 1; right child index at 2i + 2.
        if (len(self.items_list) <= 1) | (root_idx < 0):
            return

        if 2 * root_idx + 2 < len(self.items_list):  # If both children exist.
            # If parent > either child, a swap happens.
            if self.items_list[root_idx] > min(self.items_list[2 * root_idx + 1], self.items_list[2 * root_idx + 2]):
                swap_idx = 2 * root_idx + 1  # Left child's index.
                # If right child < left child, switch to right child's index. Otherwise, keep left child's index.
                if self.items_list[2 * root_idx + 2] < self.items_list[2 * root_idx + 1]:
                    swap_idx += 1

                self.items_list[root_idx], self.items_list[swap_idx] = (
                    self.items_list[swap_idx], self.items_list[root_idx])

                # Heapify special case: if subtree has both children and does a swap.
                # Jump to the subtree at swap index to ensure relative order.
                self.heapify(root_idx=swap_idx)
            return

        if 2 * root_idx + 1 < len(self.items_list):  # If just left child exists.
            # If parent > left child.
            if self.items_list[root_idx] > self.items_list[2 * root_idx + 1]:
                self.items_list[root_idx], self.items_list[2 * root_idx + 1] = (
                    self.items_list[2 * root_idx + 1], self.items_list[root_idx])

    def sort(self):
        if len(self.items_list) <= 1:
            return self.items_list

        copied_items_list = deepcopy(self.items_list)  # Deep copy self.items list for later restoration.
        sorted_list = []  # Carry sorted items.
        self.build_heap()
        while True:
            # At the start of each iteration, switch the last item with root (min item).
            self.items_list[0], self.items_list[-1] = self.items_list[-1], self.items_list[0]
            sorted_list.append(self.items_list.pop(-1))  # Add min item to sorted list.
            if len(self.items_list) <= 0:  # Only break while if self.items list becomes empty.
                break
            self.heapify()  # Otherwise, heapify for the next iteration.

        self.items_list.extend(copied_items_list)  # Restoration.
        return sorted_list

    def find_min_value(self, remove=False):
        if remove:
            root_value = self.items_list.pop(0)
            self.build_heap()  # Ensure the min item is still at root.
            return root_value
        return self.items_list[0]

    def find_median_value(self):
        if len(self.items_list) == 0:
            return None
        if len(self.items_list) == 1:
            return self.items_list[0]

        copied_items_list = deepcopy(self.items_list)  # Deep copy self.items list for later restoration.
        total_items = len(self.items_list)
        # Median is defined by rank from smallest to largest.
        median_depth = (total_items + 1) // 2 if total_items % 2 == 1 else total_items // 2

        self.build_heap()  # Build items list into min heap structure before sorting.
        for i in range(median_depth):
            # At the start of each iteration, switch the last item with root (min item).
            self.items_list[0], self.items_list[-1] = self.items_list[-1], self.items_list[0]

            if i + 1 == median_depth:  # After popping out first (median - 1) items, the next one is median.
                median = self.items_list.pop(-1)
                self.items_list.clear()  # Clear and restore.
                self.items_list.extend(copied_items_list)
                return median

            self.items_list.pop(-1)
            self.heapify()  # Heapify for the next iteration.


if __name__ == '__main__':
    import time

    start_time = time.time()
    numbers_list = [i for i in reversed(range(1, 100001))]
    min_heap = MinHeap(numbers_list)

    assert min_heap.sort() == sorted(numbers_list)
    end_time = time.time()
    print(f'Sorted list:\n{min_heap.sort()}\n')
    print(f'Total runtime: {str(round(end_time - start_time, 2))} seconds on {len(numbers_list)} items.\n')
    print(f'(From smallest to biggest) Median item: {str(min_heap.find_median_value())}.')
