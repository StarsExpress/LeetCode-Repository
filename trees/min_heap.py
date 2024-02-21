import math


class MinHeap:
    """Apply min heap to sort items."""

    def __init__(self, items_list):
        self.items_list = items_list
        self.build_heap()  # Build items list into min heap structure during initialization.

    def build_heap(self):
        total_subtrees = math.floor(len(self.items_list) / 2)
        for i in reversed(range(total_subtrees)):
            self.heapify(root_idx=i)
        del total_subtrees

    # Heapify special case: if subtree of ith index has both children and does a swap.
    # Jump to the subtree at swap index to ensure relative order.
    def heapify(self, root_idx):  # root_idx: the index where a subtree's root is.
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

                self.heapify(root_idx=swap_idx)  # Apply the special case.
            return

        if 2 * root_idx + 1 < len(self.items_list):  # If just left child exists.
            # If parent > left child.
            if self.items_list[root_idx] > self.items_list[2 * root_idx + 1]:
                self.items_list[root_idx], self.items_list[2 * root_idx + 1] = (
                    self.items_list[2 * root_idx + 1], self.items_list[root_idx])

    def sort(self):
        if len(self.items_list) <= 1:
            return self.items_list

        sorted_list = []  # Carry sorted items.
        while True:
            # At the start of each iteration, switch the last item with root (min item) in self list.
            self.items_list[0], self.items_list[-1] = self.items_list[-1], self.items_list[0]
            sorted_list.append(self.items_list.pop(-1))  # Pop out min item and add to sorted list.
            if len(self.items_list) <= 0:  # Only break while if self.items list becomes empty.
                break
            self.heapify(root_idx=0)  # Otherwise, heapify for the next iteration.

        self.items_list.extend(sorted_list)
        del sorted_list
        return self.items_list


if __name__ == '__main__':
    import time

    start_time = time.time()
    numbers_list = [i for i in reversed(range(1, 100001))]
    min_heap = MinHeap(numbers_list)
    assert min_heap.sort() == sorted(numbers_list)

    end_time = time.time()
    print(f'Sorted list:\n{min_heap.sort()}\n')
    print(f'Total runtime: {str(round(end_time - start_time, 2))} seconds on {len(numbers_list)} items.')
