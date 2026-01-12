
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node):  # LeetCode Q.237.
    node.val = node.next.val
    node.next = node.next.next
