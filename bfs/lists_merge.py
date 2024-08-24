import heapq


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class SortedLinkedListsMerge:  # LeetCode Q.23.
    def __init__(self):
        # List of digits lists and list of digits, respectively.
        self.digits_lists, self.digits, self.list_node = [], [], None

    def merge_sorted_lists(self, lists: list[ListNode | None]):
        self.digits_lists.clear()  # Reset before BFS.
        for linked_list in lists:
            self._bfs_collect_digits(linked_list, True)

        if not self.digits_lists:
            return None

        self.digits.clear()  # Reset before heap sort.
        self._heap_sort_digits()
        self.list_node = ListNode(self.digits.pop(0))
        self._bfs_build_nodes(self.list_node)
        return self.list_node

    def _bfs_collect_digits(self, node: ListNode, list_start: bool = False):
        if node is not None:
            if list_start:  # A new linked-list.
                self.digits_lists.append([])

            self.digits_lists[-1].append(node.val)
            if node.next:  # Can still extend.
                self._bfs_collect_digits(node.next)
        return

    def _bfs_build_nodes(self, list_node: ListNode):
        if self.digits:  # Still unmerged digits.
            list_node.next = ListNode(self.digits.pop(0))
            self._bfs_build_nodes(list_node.next)
        return

    def _heap_sort_digits(self):
        min_heap = []  # Keep track of smallest digits across all digits lists.

        for list_idx, digits_list in enumerate(self.digits_lists):
            if digits_list:  # Initialize heap of each non-empty list's 1st digit.
                # Tuple: (digit, list's idx, digit's idx in list).
                heapq.heappush(min_heap, (digits_list[0], list_idx, 0))

        sorted_digits = []
        while min_heap:
            digit, list_idx, digit_idx = heapq.heappop(min_heap)  # Currently smallest.
            sorted_digits.append(digit)

            if digit_idx < len(self.digits_lists[list_idx]) - 1:
                # Current digit's right side neighbor exists.
                next_digit = self.digits_lists[list_idx][digit_idx + 1]
                heapq.heappush(min_heap, (next_digit, list_idx, digit_idx + 1))

        self.digits.extend(sorted_digits)
