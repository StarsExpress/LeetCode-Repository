
class DirectedGraphVisitedNodes:  # LeetCode Q.2876.
    def __init__(self):
        self.graph = []  # -1 means a node has no outgoing edge.
        self.visit_orders = []  # -1 means a node isn't in current DFS.
        self.desc_cycle_starts = []  # -1 means a node hasn't been searched yet.
        self.distinct_visits = []  # 0 means a node hasn't been searched yet.

    def count_visited_nodes(self, edges: list[int]) -> list[int]:
        total_nodes = len(edges)
        self.graph.clear()  # Rebuild graph.
        self.graph.extend([-1] * total_nodes)
        for out_node, in_node in enumerate(edges):  # Directed edges.
            self.graph[out_node] = in_node

        self.visit_orders.clear()  # Reset before DFS.
        self.visit_orders.extend([-1] * total_nodes)

        self.desc_cycle_starts.clear()  # Reset before DFS.
        self.desc_cycle_starts.extend([-1] * total_nodes)

        self.distinct_visits.clear()  # Reset before DFS.
        self.distinct_visits.extend([0] * total_nodes)

        for node in range(total_nodes):
            if self.distinct_visits[node] == 0:  # Not searched yet.
                self._dfs_cycles(node, 1)

        return self.distinct_visits

    def _dfs_cycles(self, node: int, visit_order: int) -> tuple[int, int]:
        # Return format: (descendant cycle start, distinct visits).

        # Goes to a node that belongs to current DFS: cycle forms.
        if self.visit_orders[self.graph[node]] != -1:
            self.desc_cycle_starts[node] = self.graph[node]
            self.distinct_visits[node] = visit_order + 1 - self.visit_orders[self.graph[node]]
            return self.desc_cycle_starts[node], self.distinct_visits[node]

        # Goes to a node that already knows its distinct visits.
        if self.distinct_visits[self.graph[node]] != 0:
            self.desc_cycle_starts[node] = self.desc_cycle_starts[self.graph[node]]
            self.distinct_visits[node] = 1 + self.distinct_visits[self.graph[node]]
            return self.desc_cycle_starts[node], self.distinct_visits[node]

        self.visit_orders[node] = visit_order
        cycle_start, distinct_visits = self._dfs_cycles(self.graph[node], visit_order + 1)
        self.desc_cycle_starts[node] = cycle_start

        if self.visit_orders[cycle_start] == -1:  # Cycle start has left current DFS.
            distinct_visits += 1
        self.distinct_visits[node] = distinct_visits

        self.visit_orders[node] = -1  # Node is visited and leaves current DFS.
        return self.desc_cycle_starts[node], self.distinct_visits[node]
