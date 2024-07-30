
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxBSTSum:  # LeetCode Q.1373.
    def __init__(self):
        self.max_bst_sum = 0

    def find_max_bst_sum(self, root: TreeNode | None):
        self.max_bst_sum -= self.max_bst_sum  # Required to set 0 as floor.
        if root is not None:
            self._dfs_max_bst_sum(root)
        return self.max_bst_sum

    def _dfs_max_bst_sum(self, current_node: TreeNode) -> tuple[int | None, int | None, int | None]:
        """Valid BST: max existing left child < parent node < min existing right child."""
        if not current_node.left and not current_node.right:  # Leaf node.
            if current_node.val > self.max_bst_sum:  # Leaf node BST sets new record.
                self.max_bst_sum = current_node.val
            return current_node.val, current_node.val, current_node.val

        if current_node.left:
            left_bst_sum, left_bst_min, left_bst_max = self._dfs_max_bst_sum(current_node.left)

        else:
            left_bst_sum, left_bst_min, left_bst_max = 0, -float("inf"), -float("inf")

        if current_node.right:
            right_bst_sum, right_bst_min, right_bst_max = self._dfs_max_bst_sum(current_node.right)
            if right_bst_sum is None:  # Right descendants BST nullified.
                return None, None, None  # Stop searching.

        else:
            right_bst_sum, right_bst_min, right_bst_max = 0, float("inf"), float("inf")

        if left_bst_sum is None:  # Left descendants BST nullified.
            return None, None, None  # Stop searching.

        if not left_bst_max < current_node.val < right_bst_min:  # Current BST violates BST rule.
            return None, None, None  # Stop searching.

        # Current node's BST stands.
        current_bst_sum = left_bst_sum + right_bst_sum + current_node.val
        if current_bst_sum > self.max_bst_sum:  # Sets new record.
            self.max_bst_sum = current_bst_sum

        # Find current BST's existing (NO infinities) min & max values.
        current_bst_min, current_bst_max = current_node.val, current_node.val
        for value in {left_bst_min, left_bst_max, right_bst_min, right_bst_max}:
            if value in {-float("inf"), float("inf")}:
                continue  # Skip infinities!

            if value < current_bst_min:
                current_bst_min = value
            if value > current_bst_max:
                current_bst_max = value

        return current_bst_sum, current_bst_min, current_bst_max
