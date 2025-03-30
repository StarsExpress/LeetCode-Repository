
class LongestCycle:  # LeetCode Q.2360.
    def __init__(self):
        self.graph: list[int] = []
        self.visit_orders: list[int] = []
        self.status: list[int] = []  # 1: not searched yet; 2: now under DFS; 3: finished DFS.

    def _dfs_cycle_len(self, node: int, visit_order: int) -> int:
        self.visit_orders[node], self.status[node] = visit_order, 2
        cycle_len = -1  # Default to no cycle.

        if self.graph[node] != -1:  # Node has an outgoing edge.
            if self.status[self.graph[node]] == 1:
                cycle_len = self._dfs_cycle_len(self.graph[node], visit_order + 1)

            if self.status[self.graph[node]] == 2:  # Cycle forms.
                cycle_len = visit_order + 1 - self.visit_orders[self.graph[node]]

        self.status[node] = 3  # Current node finishes DFS.
        return cycle_len

    def compute_longest_cycle_len(self, edges: list[int]) -> int:
        self.graph.clear()  # Reset before search.
        self.visit_orders.clear()
        self.status.clear()

        self.graph.extend(edges)
        self.visit_orders.extend([-1] * len(edges))  # Default order = -1 (not searched).
        self.status.extend([1] * len(edges))  # All nodes aren't searched at the beginning.

        max_cycle_len = -1
        for out_node, in_node in enumerate(edges):  # Each node joins at most 1 cycle.
            if in_node != -1:  # Each node has at most 1 outgoing edge.
                cycle_len = self._dfs_cycle_len(out_node, 1)
                if cycle_len > max_cycle_len:
                    max_cycle_len = cycle_len

        return max_cycle_len
