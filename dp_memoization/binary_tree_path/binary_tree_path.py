
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeMaxPathSum:  # LeetCode Q.124.
    def __init__(self):
        self.max_path_sum = -1000  # Min node value stated by question.

    def find_max_path_sum(self, root: TreeNode | None):
        self._dfs_path_sum(root)
        return self.max_path_sum

    def _dfs_path_sum(self, node: TreeNode) -> int:
        left_child_path_sum, right_child_path_sum = 0, 0
        if node.left:
            left_child_path_sum += max(self._dfs_path_sum(node.left), 0)
        if node.right:
            right_child_path_sum += max(self._dfs_path_sum(node.right), 0)

        left_end_path_sum = left_child_path_sum + node.val
        middle_path_sum = left_end_path_sum + right_child_path_sum
        right_end_path_sum = node.val + right_child_path_sum

        max_path_sum = max(
            left_end_path_sum, middle_path_sum, right_end_path_sum
        )
        if max_path_sum > self.max_path_sum:
            self.max_path_sum = max_path_sum

        return max(left_end_path_sum, right_end_path_sum, 0)
