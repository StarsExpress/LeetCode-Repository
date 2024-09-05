
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def find_bottom_leftmost(root: TreeNode | None) -> int:  # LeetCode Q.513.
    if root is None:
        return -1

    bottom_leftmost = root.val
    queue = []
    if root.left:
        queue.append(root.left)
    if root.right:
        queue.append(root.right)

    if not queue:
        return bottom_leftmost

    next_level_nodes = []
    current_level_leftmost = None

    while queue:
        node = queue.pop(0)
        if current_level_leftmost is None:
            bottom_leftmost = node.val
            current_level_leftmost = node.val

        if node.left:
            next_level_nodes.append(node.left)
        if node.right:
            next_level_nodes.append(node.right)

        if not queue:  # Current level BFS is done.
            queue.extend(next_level_nodes)  # Put next level into queue.
            next_level_nodes.clear()
            current_level_leftmost = None  # Reset for next level BFS.

    return bottom_leftmost
