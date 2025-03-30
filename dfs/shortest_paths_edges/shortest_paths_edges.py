import heapq


class ShortestPathsEdges:  # LeetCode Q.3123.
    def __init__(self):
        self.graph: dict[int, set[int]] = dict()
        self.edges2indices, self.edges2weights = dict(), dict()
        self.visited: dict[int, bool] = dict()
        self.target_node, self.target_dist = 0, 0
        self.edges_existence = []

    def _dfs_edges_existence(self, node: int, dist: int) -> bool:
        if node == self.target_node:
            existence = True

        else:
            existence, self.visited[node] = False, True
            for neighbor in self.graph[node]:
                if not self.visited[neighbor]:
                    edge = f"{node}:{neighbor}"
                    weight = self.edges2weights[edge]

                    if weight + dist <= self.target_dist:
                        if self._dfs_edges_existence(neighbor, weight + dist):
                            existence = True
                            edge_idx = self.edges2indices[f"{node}:{neighbor}"]
                            self.edges_existence[edge_idx] = True

            self.visited[node] = False  # LIFO: update visit status.

        return existence

    def find_edges_existences(self, total_nodes: int, edges: list[list[int]]) -> list[bool]:
        self.graph.clear()
        self.edges2indices.clear()
        self.edges2weights.clear()

        for idx, (node_1, node_2, weight) in enumerate(edges):
            if node_1 not in self.graph.keys():  # Undirected graph.
                self.graph.update({node_1: set()})
            self.graph[node_1].add(node_2)

            if node_2 not in self.graph.keys():  # Undirected graph.
                self.graph.update({node_2: set()})
            self.graph[node_2].add(node_1)

            self.edges2indices.update(  # Undirected edge.
                {f"{node_1}:{node_2}": idx, f"{node_2}:{node_1}": idx}
            )
            self.edges2weights.update(  # Undirected edge.
                {f"{node_1}:{node_2}": weight, f"{node_2}:{node_1}": weight}
            )

        shortest_paths = [0] + [float("inf")] * (total_nodes - 1)  # From source 0 to all nodes.
        for node_1, node_2, weight in edges:
            if node_1 == 0:  # Undirected edge.
                shortest_paths[node_2] = weight
            if node_2 == 0:  # Undirected edge.
                shortest_paths[node_1] = weight

        dist_heap: list[list[int]] = []  # Min heap. Format: [distance, node].
        for node in range(total_nodes):
            if shortest_paths[node] != float("inf"):
                heapq.heappush(dist_heap, [shortest_paths[node], node])

        # Source 0 is already visited.
        self.visited.update(dict(zip(range(total_nodes), [True] + [False] * (total_nodes - 1))))

        # Early exit on closest unvisited distance: graph may be disconnected.
        while dist_heap and dist_heap[0][0] != float("inf"):
            closest_dist, closest_node = heapq.heappop(dist_heap)
            if not self.visited[closest_node]:
                shortest_paths[closest_node] = closest_dist

                for node in self.graph[closest_node]:
                    if not self.visited[node]:
                        dist = self.edges2weights[f"{closest_node}:{node}"]
                        if dist + closest_dist < shortest_paths[node]:
                            shortest_paths[node] = dist + closest_dist
                            heapq.heappush(dist_heap, [shortest_paths[node], node])

                self.visited[closest_node] = True

        self.edges_existence.clear()  # Reset and default to False.
        self.edges_existence.extend([False] * len(edges))

        if shortest_paths[total_nodes - 1] != float("inf"):  # Source can visit (n - 1)th node.
            self.target_node, self.target_dist = total_nodes - 1, shortest_paths[total_nodes - 1]
            self.visited.update(dict(zip(range(total_nodes), [False] * total_nodes)))  # Reset for DFS.
            self._dfs_edges_existence(0, 0)

        return self.edges_existence
