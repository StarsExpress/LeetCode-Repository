
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeHeight:  # LeetCode Q.2458.
    def __init__(self):
        # Min tree height for each node if node and uts ancestors exist.
        self.nodes2min_heights: dict[int, int] = dict()
        # Original tree's height, and total leaves at tree's max level.
        self.full_tree_height, self.max_level_leaves = 0, 0

        self.nodes2levels: dict[int, int] = dict()  # Each node's level.
        # Each level's top 2 min heights of nodes in this level.
        self.levels2min_heights: dict[int, list[int]] = dict()

        self.remaining_height: dict[int, int] = dict()  # Tree height if each node is removed.

    def query_height(self, root: TreeNode | None, queries: list[int]) -> list[int]:
        self.nodes2min_heights.clear()
        self.full_tree_height, self.max_level_leaves = 0, 0

        self.nodes2levels.clear()
        self.levels2min_heights = {0: []}

        self._dfs_tree_height(root, 0)
        self._dfs_max_level_leaves(root, 0)
        return [self.remaining_height[query] for query in queries]

    def _dfs_tree_height(self, node: TreeNode, height: int) -> int:
        self.nodes2levels.update({node.val: height})  # Level = height.
        if height > self.full_tree_height:
            self.full_tree_height = height  # Reset init tree height.
            self.max_level_leaves = 0  # Reset max level leaves.

            self.levels2min_heights.update({height: []})  # A new level.

        if height == self.full_tree_height:
            self.max_level_leaves += 1

        self.nodes2min_heights.update({node.val: height})
        if node.left:
            left_height = self._dfs_tree_height(node.left, height + 1)
            if left_height > self.nodes2min_heights[node.val]:
                self.nodes2min_heights[node.val] = left_height

        if node.right:
            right_height = self._dfs_tree_height(node.right, height + 1)
            if right_height > self.nodes2min_heights[node.val]:
                self.nodes2min_heights[node.val] = right_height

        self.levels2min_heights[height].append(self.nodes2min_heights[node.val])
        self.levels2min_heights[height].sort()
        if len(self.levels2min_heights[height]) > 2:
            self.levels2min_heights[height].pop(0)

        return self.nodes2min_heights[node.val]

    def _dfs_max_level_leaves(self, node: TreeNode, height: int) -> int:
        self.remaining_height[node.val] = self.full_tree_height

        max_level_leaves = 0  # Total max level leaves of the subtree rooted at current node.
        if height == self.full_tree_height:
            max_level_leaves += 1

        height += 1  # Increment for next generation.
        if node.left:
            max_level_leaves += self._dfs_max_level_leaves(node.left, height)
        if node.right:
            max_level_leaves += self._dfs_max_level_leaves(node.right, height)

        if max_level_leaves == self.max_level_leaves:
            level = self.nodes2levels[node.val]
            if len(self.levels2min_heights[level]) == 2:
                second_height = self.levels2min_heights[level][0]
                self.remaining_height[node.val] = second_height

            else:
                self.remaining_height[node.val] = level - 1

        return max_level_leaves
