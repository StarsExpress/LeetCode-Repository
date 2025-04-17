import heapq


class ListNode:
    def __init__(self, val=0, next_node=None) -> None:
        self.val = val
        self.next = next_node


def merge_sorted_lists(lists: list[ListNode | None]) -> ListNode | None:  # LeetCode Q.23.
    min_heap = []  # Format: (value, its linked list idx).

    lists_nodes = []
    for idx, node in enumerate(lists):
        if node is not None:
            heapq.heappush(min_heap, (node.val, idx))
        lists_nodes.append(node)

    sorted_list, current_node = None, None
    while min_heap:
        value, list_idx = heapq.heappop(min_heap)
        if sorted_list is None:
            sorted_list = ListNode(value)
            current_node = sorted_list

        else:
            current_node.next = ListNode(value)
            current_node = current_node.next

        lists_nodes[list_idx] = lists_nodes[list_idx].next  # Next node in this list.
        if lists_nodes[list_idx] is not None:
            heapq.heappush(min_heap, (lists_nodes[list_idx].val, list_idx))

    return sorted_list
