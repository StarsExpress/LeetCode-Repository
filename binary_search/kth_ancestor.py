import math


class KthAncestor:  # LeetCode Q.1483.
    """Tree's root is node 0. Array parent[i] is parent of ith node."""
    def __init__(self, num_nodes: int, parent: list[int]):
        self.max_ancestor_dist = int(math.log2(num_nodes)) + 1  # Max power of 2 needed.
        self.ancestors = [[-1] * self.max_ancestor_dist for _ in range(num_nodes)]

        for i in range(num_nodes):  # Initialize table with each node's parent.
            self.ancestors[i][0] = parent[i]

        for j in range(1, self.max_ancestor_dist):  # Precompute all ancestors for each node.
            for i in range(num_nodes):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]

    def get_kth_ancestor(self, node: int, k: int):
        for j in range(self.max_ancestor_dist):
            if k & (1 << j):
                node = self.ancestors[node][j]
                if node == -1:  # No ancestor.
                    return -1

        return node
