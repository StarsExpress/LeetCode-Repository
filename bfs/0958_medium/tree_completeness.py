
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def check_completeness(root: TreeNode | None) -> bool:  # LeetCode Q.958.
    if root is None:
        return False

    queue = []  # Format: (child idx at child's level, child).
    if root.left:
        queue.append((0, root.left))
    if root.right:
        queue.append((1, root.right))
    if not queue:  # Only root node.
        return True

    next_level_nodes = []
    current_level_capacity = 2  # Max nodes that current level can carry.
    current_level_count = 0  # Occurred nodes in current level.
    last_idx = None  # Last occurred node idx in current level.

    while queue:
        node_idx, node = queue.pop(0)
        current_level_count += 1

        if last_idx is not None and last_idx + 1 < node_idx:  # Gap happens.
            return False

        if last_idx is None and node_idx != 0:  # 1st occurrence not at 0th idx.
            return False

        last_idx = node_idx

        if node.left:
            next_level_nodes.append(
                (node_idx * 2, node.left)
            )
        if node.right:
            next_level_nodes.append(  # Right child idx needs to add 1.
                (node_idx * 2 + 1, node.right)
            )

        if not queue:  # Current level BFS is done. Detect incompleteness.
            if current_level_count < current_level_capacity and next_level_nodes:
                return False

            queue.extend(next_level_nodes)  # Put next level into queue.
            next_level_nodes.clear()

            current_level_capacity *= 2  # Update for next level BFS.
            current_level_count -= current_level_count  # Reset for next level BFS.
            last_idx = None

    return True  # All BFS passed. Binary tree is complete.
