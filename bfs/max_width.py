
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find_max_width(root: TreeNode | None) -> int:  # LeetCode Q.662.
    if root is None:
        return 0
    if not root.left and not root.right:  # Only root node.
        return 1

    max_width = 0
    # Format: parent idx at parent's level, left child, right child.
    queue = [(0, root.left, root.right)]
    next_level_nodes = []

    left_end_idx, right_end_idx = None, None
    while queue:
        parent_idx, left_node, right_node = queue.pop(0)
        child_nodes = [left_node, right_node]

        for i in range(2):
            if child_nodes[i]:
                child_idx = parent_idx * 2
                if i == 1:  # Right child idx needs to add 1.
                    child_idx += 1

                if left_end_idx is None:
                    left_end_idx = child_idx

                else:  # Once left end is set, not None child updates right end.
                    right_end_idx = child_idx

                if child_nodes[i].left or child_nodes[i].right:
                    next_level_nodes.append(
                        (child_idx, child_nodes[i].left, child_nodes[i].right)
                    )

        if not queue:  # Current level BFS is done.
            if left_end_idx is not None:  # Update max width if needed.
                width = 1  # Left end exists: width >= 1.
                if right_end_idx is not None:
                    width += right_end_idx - left_end_idx

                if width > max_width:
                    max_width = width

            queue.extend(next_level_nodes)  # Put next level into queue.
            next_level_nodes.clear()
            left_end_idx, right_end_idx = None, None  # Reset for next level BFS.

    return max_width
