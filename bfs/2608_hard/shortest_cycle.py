
def find_shortest_cycle(total_nodes: int, edges: list[list[int]]) -> int:  # LeetCode Q.2608.
    graph: list[set[int]] = [set() for _ in range(total_nodes)]
    for node_1, node_2 in edges:  # Undirected edges.
        graph[node_1].add(node_2)
        graph[node_2].add(node_1)

    shortest_cycle = float("inf")
    queue = []  # Format: (node, parent).
    for start_node in range(total_nodes):  # Find the shortest cycle starting from each node.
        # Each node's dist to its parent. -1 means unvisited.
        parent_dists: list[int] = [-1] * total_nodes
        parent_dists[start_node] = 0

        queue.append((start_node, start_node))
        while queue:
            node, parent = queue.pop(0)
            for neighbor in graph[node]:
                if parent != neighbor:  # Each edge must be visited just once.
                    if parent_dists[neighbor] == -1:
                        parent_dists[neighbor] = parent_dists[node] + 1
                        queue.append((neighbor, node))
                        continue

                    cycle_len = 1 + parent_dists[node] + parent_dists[neighbor]
                    if cycle_len < shortest_cycle:
                        shortest_cycle = cycle_len

    return -1 if shortest_cycle == float("inf") else shortest_cycle
