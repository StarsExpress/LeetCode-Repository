import math


class MaxHeap:
    """Apply max heap to sort items."""

    def __init__(self, items_list):
        self.items_list = items_list
        self.total_subtrees = math.floor(len(self.items_list) / 2)

    # Heapify special case: if subtree of ith idx has both children and does a swap.
    # Jump to swap idx to ensure relative order. Then go to subtree of (temp_idx - 1) idx to continue to heapify.
    def heapify(self, tree_idx=None, temp_idx=None):  # tree_idx: current subtree's index.
        # For subtree with ith idx, parent idx: i; left child idx: 2i + 1; right child idx: 2i + 2.
        if tree_idx is None:
            tree_idx = self.total_subtrees - 1  # Subtrees recursive call: from bottom to top.

        if (len(self.items_list) <= 1) | (tree_idx < 0):
            return self.items_list

        if 2 * tree_idx + 2 < len(self.items_list):  # If both children exist.
            # If parent < either child, a swap happens.
            if self.items_list[tree_idx] < max(self.items_list[2 * tree_idx + 1], self.items_list[2 * tree_idx + 2]):
                swap_idx = 2 * tree_idx + 1
                # If right child > left child, add 1 to swap idx. Otherwise, don't change.
                if self.items_list[2 * tree_idx + 2] > self.items_list[2 * tree_idx + 1]:
                    swap_idx += 1

                self.items_list[tree_idx], self.items_list[swap_idx] = (
                    self.items_list[swap_idx], self.items_list[tree_idx])

                return self.heapify(swap_idx, tree_idx)  # Apply the special case.

            if temp_idx is not None:
                return self.heapify(temp_idx - 1)
            return self.heapify(tree_idx - 1)  # Go to next subtree.

        if 2 * tree_idx + 1 < len(self.items_list):  # If just left child exists.
            # If parent < left child.
            if self.items_list[tree_idx] < self.items_list[2 * tree_idx + 1]:
                self.items_list[tree_idx], self.items_list[2 * tree_idx + 1] = (
                    self.items_list[2 * tree_idx + 1], self.items_list[tree_idx])

        if temp_idx is not None:
            return self.heapify(temp_idx - 1)
        return self.heapify(tree_idx - 1)  # Go to next subtree.

    def sort(self, sorted_list=None):
        if sorted_list is None:
            sorted_list = []  # Initiate empty sorted list.

        if len(self.items_list) <= 0:  # When all items are sorted.
            self.items_list.extend(sorted_list)
            return self.items_list

        self.heapify()  # Ensure each subtree is a max heap.
        # Swap the last item with root in self list. Now root, the max item, is at last index.
        self.items_list[0], self.items_list[-1] = self.items_list[-1], self.items_list[0]
        sorted_list.append(self.items_list.pop(-1))  # Pop out max item and add to sorted list.
        self.sort(sorted_list)
        return self.items_list


if __name__ == '__main__':
    numbers_list = [i for i in range(1, 11)]
    max_heap = MaxHeap(numbers_list)
    assert max_heap.sort() == sorted(numbers_list, reverse=True)
    print(max_heap.sort())
