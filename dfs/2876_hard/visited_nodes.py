
class DirectedGraphVisitedNodes:  # LeetCode Q.2876.
    def __init__(self):
        self.graph: list[int] = []
        self.visited_orders: list[int] = []
        self.current_order = 1
        self.visited_counts: list[int] = []

    def _dfs_visited_nodes(self, node: int) -> int:
        self.visited_orders[node] = self.current_order
        self.current_order += 1

        target_node = self.graph[node]

        # A cycle just forms. Current node and its target node are members.
        if self.visited_orders[target_node] != -1 and self.visited_counts[target_node] == 0:
            cycle_size = self.visited_orders[node] + 1 - self.visited_orders[target_node]
            self.visited_counts[node] = cycle_size
            return self.visited_orders[target_node]  # Where cycle starts.

        cycle_start_order = -1
        if self.visited_orders[target_node] == -1:
            cycle_start_order = self._dfs_visited_nodes(target_node)

        # Reset: current node is no part of any cycle. Nor are its ascendants.
        if self.visited_orders[node] < cycle_start_order:
            cycle_start_order = -1

        self.visited_counts[node] = self.visited_counts[target_node]
        if cycle_start_order == -1:
            self.visited_counts[node] += 1

        return cycle_start_order

    def count_visited_nodes(self, edges: list[int]) -> list[int]:
        self.graph = edges

        self.visited_orders = [-1] * len(edges)  # -1 means unvisited yet.
        self.current_order = 1
        self.visited_counts = [0] * len(edges)

        for node in range(len(edges)):
            if self.visited_orders[node] == -1:
                self._dfs_visited_nodes(node)

        return self.visited_counts
