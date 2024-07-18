
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxLevelSum:  # LeetCode Q.1161.
    def __init__(self):
        self.max_sum, self.max_level = None, None

    def find_max_level_sum(self, root: TreeNode | None):
        if root is None:
            return False

        self.max_sum, self.max_level = root.val, 1
        self._bfs_level_sum(root)
        return self.max_level

    def _bfs_level_sum(self, root: TreeNode | None):
        if not root.left and not root.right:  # Only root node.
            return

        queue = [(root.left, root.right)]  # Format: left child, right child.
        next_level_nodes = []

        level_sum, current_level = 0, 2
        while queue:
            child_nodes = queue.pop(0)
            for i in range(2):
                if child_nodes[i]:
                    level_sum += child_nodes[i].val

                    if child_nodes[i].left or child_nodes[i].right:
                        next_level_nodes.append(
                            (child_nodes[i].left, child_nodes[i].right)
                        )

            if not queue:  # Current level BFS is done.
                if level_sum > self.max_sum:  # Update max level sum if needed.
                    self.max_sum, self.max_level = level_sum, current_level

                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()
                level_sum = 0  # Reset for next level BFS.
                current_level += 1  # Go to next level BFS.
