
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # LeetCode Q.655.
    def __init__(self):
        self.matrix, self.total_height = [], 0

    def print_tree(self, root: TreeNode | None) -> list[list[str]]:
        self.matrix.clear()  # Reset before printing.
        if root is not None:
            self.total_height -= self.total_height  # Reset before printing.
            self._bfs_height(root)
            self._bfs_tree(root)
        return self.matrix

    def _bfs_height(self, root: TreeNode | None):
        if not root.left and not root.right:  # Only root node.
            return

        queue = []
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        next_level_nodes = []
        while queue:
            node = queue.pop(0)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

            if not queue:  # Current level BFS is done.
                self.total_height += 1
                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()

    def _bfs_tree(self, root: TreeNode | None):
        for _ in range(self.total_height + 1):  # Rows = height + 1.
            self.matrix.append([""] * (2 ** (self.total_height + 1) - 1))

        root_col_idx = len(self.matrix[0]) // 2
        self.matrix[0][root_col_idx] = str(root.val)  # Set root column idx into matrix.

        if not root.left and not root.right:  # Only root node.
            return

        queue = []  # Format: parent's row idx and column idx, child node, child left side mark.
        if root.left:
            queue.append((0, root_col_idx, root.left, True))
        if root.right:
            queue.append((0, root_col_idx, root.right, False))

        next_level_nodes = []
        while queue:
            row_idx, col_idx, child_node, left_mark = queue.pop(0)

            # Calculate child col idx first as child col idx depends on parent row idx.
            col_idx -= 2 ** (self.total_height - row_idx - 1)
            if not left_mark:  # Right child idx is further right.
                col_idx += 2 * (2 ** (self.total_height - row_idx - 1))

            row_idx += 1  # Child row idx is parent row idx + 1.
            self.matrix[row_idx][col_idx] = str(child_node.val)

            if child_node.left:
                next_level_nodes.append((row_idx, col_idx, child_node.left, True))
            if child_node.right:
                next_level_nodes.append((row_idx, col_idx, child_node.right, False))

            if not queue:  # Current level BFS is done.
                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()
