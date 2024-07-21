
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeMaxPathSum:  # LeetCode Q.124.
    def __init__(self):
        self.max_path_sum = 0

    def find_max_path_sum(self, root: TreeNode | None):
        self.max_path_sum -= self.max_path_sum  # Reset to 0 before DFS.
        if root is not None:
            self.max_path_sum += root.val  # Base case when root exists.
            self._dfs_max_path_sum(root)
        return self.max_path_sum

    def _dfs_max_path_sum(self, current_node: TreeNode):
        left_path_sum = 0
        if current_node.left:  # Always collect non-negative sum.
            left_path_sum += max(self._dfs_max_path_sum(current_node.left), 0)

        right_path_sum = 0
        if current_node.right:  # Always collect non-negative sum.
            right_path_sum += max(self._dfs_max_path_sum(current_node.right), 0)

        max_path_sum = left_path_sum + right_path_sum + current_node.val
        if max_path_sum > self.max_path_sum:  # Update max path sum w.r.t. to current node's view.
            self.max_path_sum = max_path_sum

        # Return path sum to parent node. Always return non-negative sum.
        if not current_node.left and not current_node.right:
            return max(current_node.val, 0)  # Leaf node only needs to consider itself.

        # max(left_path_sum, right_path_sum): can't take both sides.
        return max(current_node.val, current_node.val + max(left_path_sum, right_path_sum), 0)
