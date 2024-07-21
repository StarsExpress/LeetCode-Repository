
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LevelMax:  # LeetCode Q.515.
    def __init__(self):
        self.level_max = []  # Max values at each level.

    def find_level_max(self, root: TreeNode | None):
        self.level_max.clear()  # Reset before search.
        if root is not None:
            self.level_max.append(root.val)
            self._bfs_level_max(root)
        return self.level_max

    def _bfs_level_max(self, root: TreeNode | None):
        queue = []
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        if not queue:
            return

        next_level_nodes = []
        current_level_max_value = -float("inf")

        while queue:
            node = queue.pop(0)
            if node.val > current_level_max_value:
                current_level_max_value = node.val

            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

            if not queue:  # Current level BFS is done.
                self.level_max.append(current_level_max_value)

                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()
                current_level_max_value = -float("inf")  # Reset for next level BFS.
