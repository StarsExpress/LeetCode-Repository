
class LongestCycle:  # LeetCode Q.2360.
    def __init__(self):
        self.edges: list[int] = []

        # Special marks: -1 = unvisited.
        # -2 = can't help find a cycle. -3 = belongs to a cycle.
        self.visited_orders: list[int] = []

        self.current_order = 1
        self.longest_cycle = -1

    def _dfs_cycle(self, node: int) -> bool:
        self.visited_orders[node] = self.current_order
        self.current_order += 1  # Increment for the next node.

        target_node = self.edges[node]
        if target_node == -1:
            self.visited_orders[node] = -2
            return False

        if self.visited_orders[target_node] <= -2:
            self.visited_orders[node] = -2
            return False

        if self.visited_orders[target_node] == -1:
            if not self._dfs_cycle(target_node):
                self.visited_orders[node] = -2
                return False

            self.visited_orders[node] = -3  # Belongs to a cycle.
            return True

        cycle_len = self.visited_orders[node] + 1 - self.visited_orders[target_node]
        if cycle_len > self.longest_cycle:
            self.longest_cycle = cycle_len

        self.visited_orders[node] = -3  # Belongs to a cycle.
        return True

    def compute_longest_cycle_len(self, edges: list[int]) -> int:
        self.edges.clear()  # Reset before search.
        self.visited_orders.clear()
        self.current_order = 1
        self.longest_cycle = -1

        self.edges.extend(edges)
        for node, _ in enumerate(edges):
            if self.visited_orders[node] == -1:  # Unvisited yet.
                self._dfs_cycle(node)

        return self.longest_cycle
