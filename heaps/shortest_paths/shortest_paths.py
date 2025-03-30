import heapq


class ShortestPathsCalculator:  # LeetCode Q.2642.
    def __init__(self, total_nodes: int, edges: list[list[int]]):
        self.infinity = float("inf")
        self.shortest_paths: list[list[int | float]] = [
            [self.infinity] * total_nodes for _ in range(total_nodes)
        ]
        for out_node, in_node, cost in edges:  # Directed edges.
            self.shortest_paths[out_node][in_node] = cost

        for node in range(total_nodes):  # Each node's cost to itself is 0.
            self.shortest_paths[node][node] = 0

    def add_edge(self, edge: list[int]) -> None:
        out_node, in_node, cost = edge
        self.shortest_paths[out_node][in_node] = cost

    def calculate_shortest_path(self, start: int, end: int) -> int:
        cost_heap = []  # Min heap. Format: (cost, node).
        for in_node, cost in enumerate(self.shortest_paths[start]):
            if in_node != start and cost != self.infinity:
                heapq.heappush(cost_heap, (cost, in_node))

        while cost_heap and cost_heap[0][0] != self.infinity:
            min_cost, min_cost_node = heapq.heappop(cost_heap)

            for neighbor, cost in enumerate(self.shortest_paths[min_cost_node]):
                if min_cost + cost < self.shortest_paths[start][neighbor]:
                    self.shortest_paths[start][neighbor] = min_cost + cost
                    heapq.heappush(
                        cost_heap, (self.shortest_paths[start][neighbor], neighbor)
                    )

        if self.shortest_paths[start][end] == self.infinity:
            return -1
        return self.shortest_paths[start][end]
