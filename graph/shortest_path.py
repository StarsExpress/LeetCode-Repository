import os
import heapq
from config import DATA_FOLDER_PATH


no_path_dist = 1000000  # Distance for non-existing edges and upper bound of shortest path search.


def process_distances() -> list[list[int]]:
    file_path = os.path.join(DATA_FOLDER_PATH, "edges", "edges_2k.txt")
    with open(file_path, "r") as file:
        nodes = file.read().splitlines()
        file.close()

    adj_matrix = [[no_path_dist] * len(nodes) for _ in range(len(nodes))]
    for node in range(1, len(nodes) + 1):
        # Minus 1: nodes order starts from 1, not 0.
        adj_matrix[node - 1][node - 1] = 0  # Entire diagonal is 0 as it's the "self" distance.

    for node in nodes:
        dist_list = (node.lstrip().rstrip().split("\t"))  # Remove boundary spaces and split by \t.
        node_1 = int(dist_list.pop(0))

        for dist_str in dist_list:
            node_2, dist = dist_str.split(",")
            node_2, dist = int(node_2), int(dist)

            adj_matrix[node_1 - 1][node_2 - 1] = dist  # Minus 1: nodes order starts from 1, not 0.
            adj_matrix[node_2 - 1][node_1 - 1] = dist

    return adj_matrix


def find_shortest_path(adj_matrix:  list[list[int]], source_node: int) -> dict[int, int]:
    total_nodes = len(adj_matrix)  # Nodes orders start from 1, not 0. Nodes minus 1 become indices.

    if source_node < 1 or source_node > total_nodes:  # Source node isn't in adjacency matrix.
        raise ValueError("Source node not found in adjacency matrix.")

    # Shortest paths from source node to all nodes. Keys: nodes. Values: shortest distances.
    shortest_paths: dict[int, int] = dict()
    for idx, dist in enumerate(adj_matrix[source_node - 1]):
        shortest_paths[idx + 1] = dist  # Node = idx + 1.

    dist_heap: list[list[int]] = []  # Min heap. Format: [distance, node].
    for node in range(1, total_nodes + 1):
        if node != source_node and shortest_paths[node] < no_path_dist:
            heapq.heappush(dist_heap, [shortest_paths[node], node])

    while dist_heap and dist_heap[0][0] != no_path_dist:  # In case of disconnected graph.
        closest_dist, closest_node = heapq.heappop(dist_heap)
        for idx, dist in enumerate(adj_matrix[closest_node - 1]):
            node = idx + 1
            if closest_dist + dist < shortest_paths[node]:
                shortest_paths[node] = closest_dist + dist
                heapq.heappush(dist_heap, [shortest_paths[node], node])

    return shortest_paths


if __name__ == "__main__":
    source, destinations = 1, [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    shortest_paths_distances = find_shortest_path(process_distances(), source)

    distances_str = ""
    if shortest_paths_distances:
        for destination in destinations:
            distances_str += str(shortest_paths_distances[destination])
            if destinations[-1] != destination:
                distances_str += ","

    print(f"Distances from {source} to each of {destinations}:\n{distances_str}")
