
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BottomLeftmostValue:  # LeetCode Q.513.
    def __init__(self):
        self.leftmost = None

    def find_bottom_leftmost(self, root: TreeNode | None):
        if root is None:
            return -1

        self.leftmost = root.val
        self._bfs_bottom_leftmost(root)
        return self.leftmost

    def _bfs_bottom_leftmost(self, root: TreeNode | None):
        queue = []
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        if not queue:
            return

        next_level_nodes = []
        current_level_leftmost_value = None

        while queue:
            node = queue.pop(0)
            if current_level_leftmost_value is None:
                self.leftmost = node.val
                current_level_leftmost_value = node.val

            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

            if not queue:  # Current level BFS is done.
                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()
                current_level_leftmost_value = None  # Reset for next level BFS.
