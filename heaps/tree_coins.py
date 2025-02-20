import heapq


def place_coins(self, edges: list[list[int]], cost: list[int]) -> list[int]:  # LeetCode 2973.
    self.graph = dict()
    for node_1, node_2 in edges:  # Undirected graph: two-sided edges.
        if node_1 not in self.graph.keys():
            self.graph.update({node_1: set()})
        self.graph[node_1].add(node_2)

        if node_2 not in self.graph.keys():
            self.graph.update({node_2: set()})
        self.graph[node_2].add(node_1)

    self.processed_nodes = set()  # Mark all the nodes already visited.
    self.coins, self.cost = [0] * len(cost), cost
    self._dfs_coins(0)  # Always start at root 0.
    return self.coins

def _dfs_coins(self, node: int) -> tuple[list[int], list[int]]:
    self.processed_nodes.add(node)

    max_heap, min_heap = [], []
    if node in self.graph.keys():
        for child_node in self.graph[node]:
            if child_node not in self.processed_nodes:
                positive_costs, negative_costs = self._dfs_coins(child_node)
                for positive_cost in positive_costs:
                    heapq.heappush(max_heap, positive_cost)

                for negative_cost in negative_costs:
                    heapq.heappush(min_heap, negative_cost)

    if self.cost[node] >= 0:  # Negate cost to fit into max heap.
        heapq.heappush(max_heap, -self.cost[node])

    else:
        heapq.heappush(min_heap, self.cost[node])

    subtree_positive_costs, subtree_negative_costs = [], []
    while max_heap and len(subtree_positive_costs) < 3:  # Only need top 3 negative.
        subtree_positive_costs.append(heapq.heappop(max_heap))

    while min_heap and len(subtree_negative_costs) < 3:  # Only need top 3 negative.
        subtree_negative_costs.append(heapq.heappop(min_heap))

    if len(subtree_positive_costs) + len(subtree_negative_costs) < 3:
        self.coins[node] += 1

    else:
        costs = subtree_negative_costs.copy()  # Use copy to prevent modification.
        costs.extend(  # Negate to original sign and stay in ascending order.
            [-cost for cost in subtree_positive_costs[::-1]]
        )

        self.coins[node] += max(
            0,  # Max triple product has 0 as its floor.
            costs[0] * costs[1] * costs[len(costs) - 1],
            costs[len(costs) - 3] * costs[len(costs) - 2] * costs[len(costs) - 1]
        )

    return subtree_positive_costs, subtree_negative_costs
