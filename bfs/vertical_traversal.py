
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class VerticalTraversal:  # LeetCode Q.987.
    def __init__(self) -> None:
        self.visited_nodes = []

    def find_vertical_traversal(self, root: TreeNode | None) -> list[list[int]]:
        vertical_traversal = []
        if root is not None:
            self.visited_nodes.clear()  # Reset before BFS.
            self.visited_nodes = [(0, 0, root.val)]  # Format: (col idx, row idx, node value).
            self._bfs_visit_nodes(root)

            columns_table = dict()
            while self.visited_nodes:
                col_idx, row_idx, node_value = self.visited_nodes.pop()
                try:
                    columns_table[col_idx]

                except KeyError:
                    columns_table.update({col_idx: []})

                columns_table[col_idx].append((row_idx, node_value))

            columns_table = sorted(columns_table.items())
            while columns_table:
                _, row_indices_values = columns_table.pop(0)
                row_indices_values.sort()
                vertical_traversal.append([indices_values[1] for indices_values in row_indices_values])

        return vertical_traversal

    def _bfs_visit_nodes(self, root: TreeNode | None) -> None:
        queue = []  # Format: (col idx, row idx, node).
        if root.left:
            queue.append((-1, 1, root.left))
        if root.right:
            queue.append((1, 1, root.right))

        if not queue:
            return

        next_level_nodes = []
        while queue:
            col_idx, row_idx, node = queue.pop(0)
            self.visited_nodes.append((col_idx, row_idx, node.val))

            if node.left:
                next_level_nodes.append((col_idx - 1, row_idx + 1, node.left))
            if node.right:
                next_level_nodes.append((col_idx + 1, row_idx + 1, node.right))

            if not queue:  # Current level BFS is done.
                queue.extend(next_level_nodes)  # Put next level into queue.
                next_level_nodes.clear()

        return
