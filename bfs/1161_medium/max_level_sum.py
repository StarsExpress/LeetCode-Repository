
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find_max_level_sum(root: TreeNode | None) -> int:  # LeetCode Q.1161.
    max_sum, max_level = root.val, 1
    if not root.left and not root.right:  # Only root node.
        return max_level

    queue = []
    if root.left:
        queue.append(root.left)
    if root.right:
        queue.append(root.right)

    next_level_nodes = []
    level_sum, current_level = 0, 2
    while queue:
        node = queue.pop(0)
        level_sum += node.val

        if node.left:
            next_level_nodes.append(node.left)
        if node.right:
            next_level_nodes.append(node.right)

        if not queue:  # Current level BFS is done.
            if level_sum > max_sum:  # Update max level sum if needed.
                max_sum, max_level = level_sum, current_level

            queue.extend(next_level_nodes)  # Put next level into queue.
            next_level_nodes.clear()
            level_sum = 0  # Reset for next level BFS.
            current_level += 1  # Go to next level BFS.

    return max_level
