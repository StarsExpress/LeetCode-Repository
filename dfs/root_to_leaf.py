
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RootToLeaf:  # LeetCode Q.129.
    """
    Each root-to-leaf path in binary tree represents a number.
    For example, root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    Return total sum of all root-to-leaf numbers.
    """
    def __init__(self, root: TreeNode | None):
        self.root, self.paths_sum = root, 0

    def sum_digits(self):
        if self.root is None:
            return 0

        self._dfs_descendants_digits(self.root, "")
        return self.paths_sum

    def _dfs_descendants_digits(self, current_node: TreeNode, path_digits: str):
        path_digits += str(current_node.val)
        if current_node.left:
            self._dfs_descendants_digits(current_node.left, path_digits)

        if current_node.right:
            self._dfs_descendants_digits(current_node.right, path_digits)

        # Leaf node: current path reaches end.
        if not current_node.left and not current_node.right:
            self.paths_sum += int(path_digits)

        return
