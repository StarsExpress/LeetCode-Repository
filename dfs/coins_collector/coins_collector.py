
class CoinsCollector:  # LeetCode Q.2603.
    def __init__(self):
        self.graph: list[set[int]] = []
        self.leaves: list[bool] = []
        self.leaves_parents: list[bool] = []

        self.empty_parents: set[int] = set()
        self.max_empty_parents_dist = 1

        self.required_visits: list[bool] = []
        self.visited: list[bool] = []
        self.must_visit_edges = 0

    def _dfs_required_visit_nodes(self, node: int) -> None:
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if self.leaves_parents[neighbor] and not self.visited[neighbor]:
                self.required_visits[node] = True
                self._dfs_required_visit_nodes(neighbor)

    def _dfs_must_visit_edges(self, parent: int, node: int) -> bool:
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                if self._dfs_must_visit_edges(node, neighbor):
                    self.required_visits[node] = True

        if self.required_visits[node] and parent != -1:
            self.must_visit_edges += 1
        return self.required_visits[node]

    def _dfs_max_empty_parents_dist(self, node: int) -> int:
        self.visited[node] = True
        children_dists: list[int] = []
        for neighbor in self.graph[node]:
            if neighbor in self.empty_parents:
                if not self.visited[neighbor]:
                    children_dists.append(self._dfs_max_empty_parents_dist(neighbor))

        local_max_dist = 1
        if not children_dists:
            return local_max_dist

        children_dists.sort()
        local_max_dist = children_dists[-1]

        if len(children_dists) >= 2:
            local_max_dist += children_dists[-2]

        if local_max_dist > self.max_empty_parents_dist:
            self.max_empty_parents_dist = local_max_dist

        return children_dists[-1] + 1

    def collect_coins(self, coins: list[int], edges: list[list[int]]) -> int:
        self.graph.clear()
        self.graph.extend([set() for _ in range(len(coins))])
        for node_1, node_2 in edges:  # Undirected edges.
            self.graph[node_1].add(node_2)
            self.graph[node_2].add(node_1)

        for node, coin in enumerate(coins):
            while coin == 0 and len(self.graph[node]) == 1:
                # Graph reduction: keep removing leaves w/o coins.
                neighbor = list(self.graph[node])[0]
                self.graph[neighbor].remove(node)
                self.graph[node].clear()
                node, coin = neighbor, coins[neighbor]

        self.leaves.clear()
        self.leaves.extend([False] * len(coins))
        self.leaves_parents.clear()
        self.leaves_parents.extend([False] * len(coins))
        for node in range(len(coins)):
            if coins[node] == 1 and len(self.graph[node]) == 1:
                self.leaves[node] = True

                neighbor = list(self.graph[node])[0]
                if coins[neighbor] == 0 or len(self.graph[neighbor]) > 1:
                    self.leaves_parents[neighbor] = True

        self.empty_parents.clear()
        self.max_empty_parents_dist = 1

        self.required_visits.clear()
        self.required_visits.extend([False] * len(coins))
        for node in range(len(coins)):
            if self.leaves_parents[node]:
                is_empty_parent = True

                for neighbor in self.graph[node]:
                    if not self.leaves_parents[neighbor] and not self.leaves[neighbor]:
                        self.required_visits[neighbor] = True
                        is_empty_parent = False

                if is_empty_parent:
                    self.empty_parents.add(node)

        if True not in self.required_visits:
            if not self.empty_parents:
                return 0

            self.visited.clear()
            self.visited.extend([False] * len(coins))
            self._dfs_max_empty_parents_dist(list(self.empty_parents)[0])
            return max(0, (self.max_empty_parents_dist - 2) * 2)

        self.visited.clear()
        self.visited.extend([False] * len(coins))
        must_visit_node = -1
        for node in range(len(coins)):
            if self.required_visits[node] and not self.visited[node]:
                must_visit_node = node
                self._dfs_required_visit_nodes(node)

        if must_visit_node != -1:
            self.must_visit_edges = 0
            self.visited.clear()
            self.visited.extend([False] * len(coins))
            self._dfs_must_visit_edges(-1, must_visit_node)

        return self.must_visit_edges * 2
