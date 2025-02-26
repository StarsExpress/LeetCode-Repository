
class FrogPosition:  # LeetCode Q.1377.
    def __init__(self):
        self.target_time, self.target_node = 0, 0
        self.graph, self.visited_nodes, self.target_time_t_prob = dict(), dict(), 0

    def find_position(self, edges: list[list[int]], time: int, node: int) -> float:
        self.target_time, self.target_node = time, node
        self.graph.clear()  # Reset before DFS.
        self.visited_nodes.clear()
        self.target_time_t_prob = 0

        for node_1, node_2 in edges:  # Undirected edges.
            if node_1 not in self.graph.keys():
                self.graph.update({node_1: set()})
            self.graph[node_1].add(node_2)

            if node_2 not in self.graph.keys():
                self.graph.update({node_2: set()})
            self.graph[node_2].add(node_1)

        self._dfs_probability(1, 0, 1)
        return self.target_time_t_prob


    def _dfs_probability(self, node: int, time: int, probability: float) -> None:
        if time == self.target_time and node == self.target_node:
            self.target_time_t_prob += probability

        time += 1
        if time <= self.target_time:
            unvisited_neighbors: set[int] = set()
            if node in self.graph.keys():
                for neighbor in self.graph[node]:
                    if neighbor not in self.visited_nodes.keys():
                        unvisited_neighbors.add(neighbor)

            if not unvisited_neighbors and node == self.target_node:
                self.target_time_t_prob += probability  # Will forever stay at target node.
                return

            self.visited_nodes.update({node: True})  # Need to keep doing DFS.
            denominator = len(unvisited_neighbors)
            for neighbor in unvisited_neighbors:
                self._dfs_probability(neighbor, time, probability / denominator)

            del self.visited_nodes[node]  # DFS ends.
