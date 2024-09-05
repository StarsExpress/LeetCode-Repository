
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def _bfs_height(root: TreeNode | None) -> int:
    total_height = 0
    if not root.left and not root.right:  # Only root node.
        return total_height

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
            total_height += 1
            queue.extend(next_level_nodes)  # Put next level into queue.
            next_level_nodes.clear()

    return total_height


def print_tree(self, root: TreeNode | None) -> list[list[str]]:  # LeetCode Q.655.
    matrix = []
    total_height = self._bfs_height(root)
    for _ in range(total_height + 1):
        matrix.append([""] * (2 ** (total_height + 1) - 1))

    root_col_idx = len(matrix[0]) // 2
    matrix[0][root_col_idx] += str(root.val)  # Set root column idx into matrix.

    if not root.left and not root.right:  # Only root node.
        return matrix

    queue = []
    # Format: (parent's row idx and column idx, child node, child left side mark).
    if root.left:
        queue.append((0, root_col_idx, root.left, True))
    if root.right:
        queue.append((0, root_col_idx, root.right, False))

    next_level_nodes = []
    while queue:
        row_idx, col_idx, child_node, left_mark = queue.pop(0)

        col_idx -= 2 ** (total_height - row_idx - 1)
        if not left_mark:  # Right child idx is further right.
            col_idx += 2 * (2 ** (total_height - row_idx - 1))

        row_idx += 1
        matrix[row_idx][col_idx] += str(child_node.val)

        if child_node.left:
            next_level_nodes.append((row_idx, col_idx, child_node.left, True))
        if child_node.right:
            next_level_nodes.append((row_idx, col_idx, child_node.right, False))

        if not queue:  # Current level BFS is done.
            queue.extend(next_level_nodes)  # Put next level into queue.
            next_level_nodes.clear()

    return matrix
