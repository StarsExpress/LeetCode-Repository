
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSum:  # LeetCode Q.113.
    """
    Given root of a binary tree and an int target_sum,
    return all root-to-leaf paths where sum of node values in the path equals target_sum.
    """
    def __init__(self, root: TreeNode | None, target_sum: int):
        self.root = root
        self.target_sum, self.paths = target_sum, []

    def find_path_sum(self):
        if self.root is None:
            return []
        self._dfs_descendants_values(self.root, [])
        return self.paths

    def _dfs_descendants_values(self, current_node: TreeNode, path: list[int]):
        path.append(current_node.val)
        if current_node.left:
            self._dfs_descendants_values(current_node.left, path)

        if current_node.right:
            self._dfs_descendants_values(current_node.right, path)

        # Leaf node: decide if current path qualifies.
        if not current_node.left and not current_node.right:
            if sum(path) == self.target_sum:
                self.paths.append(path.copy())

        path.pop(-1)  # Reset path to its state right before visiting current node.
        return
