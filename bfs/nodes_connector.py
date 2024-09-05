
class Node:
    def __init__(self, val=0, left=None, right=None, next_node=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next_node


def connect_nodes(root: Node | None) -> Node | None:  # LeetCode Q.116 & 117.
    """Connect nodes at same level in any binary tree."""
    if root is None:
        return root

    # In queue, nodes of same parent are in same tuple. Format: (left child, right child).
    queue = [(root, None)]  # Current level nodes.
    next_level_nodes = []

    while queue:
        left_node, right_node = queue.pop(0)

        if left_node:
            if right_node:
                left_node.next = right_node

            if not right_node and queue:
                if queue[0][0]:  # Queue's 1st left child.
                    left_node.next = queue[0][0]

                if not queue[0][0] and queue[0][1]:
                    left_node.next = queue[0][1]  # Queue's 1st right child.

            if left_node.left or left_node.right:
                next_level_nodes.append(
                    (left_node.left, left_node.right)
                )

        if right_node:
            if queue and queue[0][0]:  # Queue's 1st left child.
                right_node.next = queue[0][0]

            if queue and queue[0][0] is None and queue[0][1]:
                right_node.next = queue[0][1]  # Queue's 1st right child.

            if right_node.left or right_node.right:
                next_level_nodes.append(
                    (right_node.left, right_node.right)
                )

        if not queue:  # BFS search has cleared current level.
            queue.extend(next_level_nodes)  # Next level's nodes can join.
            next_level_nodes.clear()

    return root
