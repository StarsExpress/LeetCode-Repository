
class MaxHeap:
    """Apply max heap to sort items."""

    def __init__(self, items: list | tuple):
        self.items_list = []
        self.items_list.extend(items)

    def build_heap(self):  # Ensure the max item is at root.
        total_subtrees = len(self.items_list) // 2
        for i in range(total_subtrees - 1, -1, -1):  # Subtrees iterate from bottom to top.
            self.heapify(root_idx=i)

    def heapify(self, root_idx: int = 0):  # Subtree's root index has default of uppermost subtree's index.
        # Root index at ith: left child index at 2i + 1; right child index at 2i + 2.
        if (len(self.items_list) <= 1) | (root_idx < 0):
            return

        if 2 * root_idx + 2 < len(self.items_list):  # If both children exist.
            # If parent < either child, a swap happens.
            if self.items_list[root_idx] < max(self.items_list[2 * root_idx + 1], self.items_list[2 * root_idx + 2]):
                swap_idx = 2 * root_idx + 1  # Left child's index.
                # If right child > left child, switch to right child's index. Otherwise, keep left child's index.
                if self.items_list[2 * root_idx + 2] > self.items_list[2 * root_idx + 1]:
                    swap_idx += 1

                self.items_list[root_idx], self.items_list[swap_idx] = (
                    self.items_list[swap_idx], self.items_list[root_idx])

                # Heapify special case: if subtree has both children and does a swap.
                self.heapify(root_idx=swap_idx)  # Jump to the subtree at swap index to ensure relative order.
            return

        if 2 * root_idx + 1 < len(self.items_list):  # If just left child exists.
            # If parent < left child.
            if self.items_list[root_idx] < self.items_list[2 * root_idx + 1]:
                self.items_list[root_idx], self.items_list[2 * root_idx + 1] = (
                    self.items_list[2 * root_idx + 1], self.items_list[root_idx])

    def add_items(self, items, reset=False):
        if isinstance(items, dict):
            return
        if reset:
            self.items_list.clear()

        if isinstance(items, list) | isinstance(items, tuple):
            self.items_list.extend(items)

        else:
            self.items_list.append(items)

    def find_max(self, remove=False):
        self.build_heap()  # Ensure the max item is still at root.
        if remove:
            return self.items_list.pop(0)
        return self.items_list[0]

    def sort(self):
        if len(self.items_list) <= 1:
            return self.items_list

        sorted_list = []  # Carry sorted items.
        self.build_heap()
        while True:
            # At the start of each iteration, switch the last item with root (max item).
            self.items_list[0], self.items_list[-1] = self.items_list[-1], self.items_list[0]
            sorted_list.append(self.items_list.pop(-1))  # Add max item to sorted list.
            if len(self.items_list) <= 0:  # Only break while if self.items list becomes empty.
                break
            self.heapify()  # Otherwise, heapify for the next iteration.

        self.items_list.extend(sorted_list)
        return self.items_list


if __name__ == '__main__':
    import time

    numbers_list = [i for i in range(1, 1000001)]
    max_heap = MaxHeap(numbers_list)

    start_time = time.time()
    print(f'Sorted list:\n{max_heap.sort()}\n')
    end_time = time.time()
    print(f'Total runtime: {str(round(end_time - start_time, 2))} seconds on {len(numbers_list)} items.\n')
