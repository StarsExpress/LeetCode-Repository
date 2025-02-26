
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeCameras:  # LeetCode Q.968.
    def __init__(self):
        self.total_cameras = 0

    def count_min_cameras(self, root: TreeNode) -> int:
        self.total_cameras -= self.total_cameras  # Reset before DFS.
        self._dfs_cameras(root, False)
        return self.total_cameras

    def _dfs_cameras(self, node: TreeNode, have_parent: bool = True) -> int:
        # Status: 0 is uncovered; 1 is covered with self camara.
        # 2 is covered with child(ren) camera(s).
        # Default child status is 2: child is covered but can't cover its parent.

        left_child_status = 2
        if node.left:
            left_child_status = self._dfs_cameras(node.left)

        right_child_status = 2
        if node.right:
            right_child_status = self._dfs_cameras(node.right)

        if min(left_child_status, right_child_status) == 0:
            self.total_cameras += 1  # Current node must cover for its child(ren).
            return 1

        if min(left_child_status, right_child_status) == 1:
            return 2  # Current node is covered by child(ren)'s camera(s).

        # Current node has no coverage from its child(ren).
        if have_parent:  # Ask parent for coverage.
            return 0

        self.total_cameras += 1  # No parent: must cover itself.
        return 1
