
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class TreeFlattener:  # LeetCode Q.114.
    """Flatten a binary tree to a linked list in-place."""
    def __init__(self) -> None:
        self.visited_values = []

    def flatten(self, tree: TreeNode | None) -> None:
        """Flatten tree in-place."""
        if tree is None:
            return

        self.visited_values.clear()  # Reset before flattening.
        self._dfs_visit_values(tree)
        self.visited_values.pop(0)  # 1st value is already root.val. It doesn't need changes.

        tree.left = None
        tree_node = tree
        for value in self.visited_values:
            tree_node.right = TreeNode(value, None, None)
            tree_node = tree_node.right

    def _dfs_visit_values(self, node: TreeNode) -> None:
        self.visited_values.append(node.val)
        if node.left:
            self._dfs_visit_values(node.left)
        if node.right:
            self._dfs_visit_values(node.right)
        return
