
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BottomLeftmostValue:  # LeetCode Q.513.
    def __init__(self):
        self.leftmost = dict()

    def find_bottom_leftmost(self, root: TreeNode | None):
        # Left streak: number of "consecutive" left edges starting from root in a path.
        self.leftmost.update({"edges": 0, "value": root.val, "left_streak": 0})
        self._dfs_descendants_values(root, -1, -1, True, False)
        return self.leftmost["value"]

    def _dfs_descendants_values(
        self,
        current_node: TreeNode,
        edges: int,
        left_streak: int,
        from_left: bool,
        streak_end: bool,
    ):
        edges += 1  # One more edge visited.
        if from_left and not streak_end:
            left_streak += 1

        if current_node.left:
            self._dfs_descendants_values(current_node.left, edges, left_streak, True, streak_end)

        if current_node.right:
            self._dfs_descendants_values(current_node.right, edges, left_streak, False, True)

        # Leaf node: decide if leftmost value needs updates.
        if not current_node.left and not current_node.right:
            if edges > self.leftmost["edges"]:
                self.leftmost.update(
                    {
                        "edges": edges,
                        "value": current_node.val,
                        "left_streak": left_streak
                    }
                )

            elif edges == self.leftmost["edges"]:
                if left_streak > self.leftmost["left_streak"]:
                    self.leftmost.update(
                        {"value": current_node.val, "left_streak": left_streak}
                    )
