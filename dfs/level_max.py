
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LevelMax:  # LeetCode Q.515.
    def __init__(self):
        pass

    def find_level_max(self, root: TreeNode | None):
        if root is None:
            return []

        level_max = dict()  # Each level's max value.
        self._dfs_descendants_max(root, 0, level_max)
        return list(level_max.values())

    def _dfs_descendants_max(
        self, current_node: TreeNode, path_edges: int, level_max: dict[int, int]
    ):
        """
        Path edges = edges count from root to current node. Plus 1 gets current node level.
        """
        path_edges += 1
        if path_edges not in level_max.keys():
            level_max.update({path_edges: current_node.val})

        if current_node.val > level_max[path_edges]:
            level_max.update({path_edges: current_node.val})

        if current_node.left:
            self._dfs_descendants_max(current_node.left, path_edges, level_max)

        if current_node.right:
            self._dfs_descendants_max(current_node.right, path_edges, level_max)
