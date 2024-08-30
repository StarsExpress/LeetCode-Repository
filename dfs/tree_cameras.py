
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _dfs_cameras(node: TreeNode | None):
    if not node:
        return 0

    required_cameras = _dfs_cameras(node.left) + _dfs_cameras(node.right)
    left_status = node.left.val if node.left else float("inf")
    right_status = node.right.val if node.right else float("inf")

    if min(left_status, right_status) == 0:
        node.val = 1
        required_cameras += 1

    if min(left_status, right_status) == 1:
        node.val = 2

    return required_cameras


def count_min_cameras(root: TreeNode | None):  # LeetCode Q.968.
    return _dfs_cameras(root) + (root.val == 0)
