
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeFlattener:  # LeetCode Q.114.
    """Flatten a binary tree to a linked list in-place."""
    def __init__(self, tree: TreeNode | None):
        self.tree = tree

    def flatten(self):
        """Flatten tree in-place."""
        if self.tree is None:
            return

        visited_values = []
        self._dfs_visit_values(self.tree, visited_values)

        # In-place modification: 1st value is already root.val. Doesn't need changes.
        visited_values.pop(0)
        tree_node = self.tree
        while visited_values:
            tree_node.left = None  # Linked list puts values in right.
            tree_node.right = TreeNode(visited_values.pop(0), None, None)
            tree_node = tree_node.right

    def _dfs_visit_values(self, current_node: TreeNode, visited_values: list[int]):
        visited_values.append(current_node.val)
        if current_node.left:
            self._dfs_visit_values(current_node.left, visited_values)

        if current_node.right:
            self._dfs_visit_values(current_node.right, visited_values)

        return  # Both left & right paths are None.
