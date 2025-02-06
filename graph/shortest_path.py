import os
import heapq
from config import DATA_FOLDER_PATH


no_path_dist = 1000000  # Distance for non-existing edges and upper bound of shortest path search.


def process_distances() -> list[list[int]]:
    file_path = os.path.join(DATA_FOLDER_PATH, "edges", "edges_2k.txt")
    with open(file_path, "r") as file:
        nodes = file.read().splitlines()
        file.close()

    adjacency_matrix = [[no_path_dist] * len(nodes) for _ in range(len(nodes))]
    for i in range(len(nodes)):
        adjacency_matrix[i][i] = 0  # Entire diagonal is 0 as it's the "self" distance.

    visited_edges = set()
    for node in nodes:
        dist_list = (node.lstrip().rstrip().split("\t"))  # Remove boundary spaces and split by \t.
        pivot_node = int(dist_list.pop(0))  # 1st item of list is pivot node. Convert to integer.

        for dist_str in dist_list:  # The rest items indicate distances between pivot node and other nodes,
            destination_node, dist = dist_str.split(",")
            destination_node, dist = int(destination_node), int(dist)

            # Edge format: smaller node on left, and bigger node on right.
            edge = (min([pivot_node, destination_node]), max([pivot_node, destination_node]))
            if edge not in visited_edges:  # Store unvisited edge distance into matrix.
                # Minus 1: nodes order starts from 1, not 0.
                adjacency_matrix[pivot_node - 1][destination_node - 1] = dist
                adjacency_matrix[destination_node - 1][pivot_node - 1] = dist

    return adjacency_matrix


def find_shortest_path(adjacency_matrix:  list[list[int]], source_node: int) -> dict[int, int]:
    # Nodes order starts from 1, not 0. Indexing needs +/- 1.
    total_nodes = len(adjacency_matrix)
    if source_node < 1 or source_node > total_nodes:  # Source node isn't in adjacency matrix.
        raise ValueError("Source node not found in adjacency matrix.")

    shortest_paths: dict[int, int] = dict()  # Shortest paths from source node to all nodes.
    distances_heap: list[list[int, int]] = []  # Min heap. Format: [distance, node].
    for i in range(total_nodes):
        shortest_paths.update({i + 1: adjacency_matrix[source_node - 1][i]})
        heapq.heappush(distances_heap, [adjacency_matrix[source_node - 1][i], i + 1])

    visited_nodes = {source_node}  # Source is already visited.
    while distances_heap:
        closest_dist, closest_node = heapq.heappop(distances_heap)
        if closest_node not in visited_nodes:
            shortest_paths.update({closest_node: closest_dist})  # Closest unvisited node to source.

            for node in shortest_paths.keys():  # Update distances from min node to other nodes.
                if adjacency_matrix[closest_node - 1][node - 1] + closest_dist < shortest_paths[node]:
                    adjacency_matrix[closest_node - 1][node - 1] += closest_dist
                    shortest_paths.update(
                        {node: adjacency_matrix[closest_node - 1][node - 1]}
                    )
                    heapq.heappush(
                        distances_heap, [adjacency_matrix[closest_node - 1][node - 1], node]
                    )

            visited_nodes.add(closest_node)  # This closest unvisited node becomes visited.

    return shortest_paths


if __name__ == "__main__":
    source, destinations = 1, [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    shortest_paths_dictionary = find_shortest_path(process_distances(), source)

    distances_str = ""
    if shortest_paths_dictionary:
        for destination in destinations:
            distances_str += str(shortest_paths_dictionary[destination])
            if destinations[-1] != destination:
                distances_str += ","

    print(f"Distances from {source} to each of {destinations}:\n{distances_str}")
