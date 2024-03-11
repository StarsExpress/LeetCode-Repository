from config import DATA_FOLDER_PATH
import os


no_path_dist = 1000000  # Distance for non-existing edges and upper bound of shortest path search.


def process_distances():
    file_path = os.path.join(DATA_FOLDER_PATH, 'edges_2k.txt')
    with open(file_path, 'r') as file:
        nodes = file.read().splitlines()
        file.close()

    adjacency_matrix = [[no_path_dist] * len(nodes) for _ in range(len(nodes))]
    for i in range(len(nodes)):  # The entire diagonal should be 0 as it's the "self" distance.
        adjacency_matrix[i][i] = 0

    visited_edges_set = set()
    for node in nodes:
        dist_list = node.lstrip().rstrip().split('\t')  # Remove boundary spaces and split by \t.
        pivot_node = int(dist_list.pop(0))  # 1st item of list is pivot node. Convert to integer.

        for dist_str in dist_list:  # The rest items indicate distances between pivot node and other nodes,
            (destination_node, dist) = dist_str.split(',')
            destination_node, dist = int(destination_node), int(dist)  # Convert to integer.

            # Edge format: the smaller one on left, and the bigger one on right.
            edge = (min([pivot_node, destination_node]), max([pivot_node, destination_node]))

            if edge not in visited_edges_set:  # Store unvisited edge' distance into matrix.
                # Minus 1: nodes order starts from 1, not 0.
                adjacency_matrix[pivot_node - 1][destination_node - 1] = dist
                adjacency_matrix[destination_node - 1][pivot_node - 1] = dist

    del file, file_path, visited_edges_set, node, nodes, dist_list, pivot_node, destination_node, dist
    return adjacency_matrix


def find_closest_unvisited_node(shortest_paths_dict, visited_nodes_set):
    closest_dist, closest_node = no_path_dist, None
    unvisited_nodes_set = set(shortest_paths_dict.keys()) - visited_nodes_set

    for unvisited_node in unvisited_nodes_set:
        if shortest_paths_dict[unvisited_node] < closest_dist:
            closest_dist, closest_node = shortest_paths_dict[unvisited_node], unvisited_node

    del unvisited_nodes_set, shortest_paths_dict, visited_nodes_set
    return closest_dist, closest_node


def find_shortest_path(adjacency_matrix, source_node):
    # Nodes order starts from 1, not 0. Indexing needs +/- 1.
    if (source_node < 1) | (source_node > len(adjacency_matrix)):  # Source node isn't in adjacency matrix.
        return dict()

    shortest_paths_dict = dict()  # Dictionary of shortest paths from source node to all nodes.
    for i in range(len(adjacency_matrix)):
        shortest_paths_dict.update({i + 1: adjacency_matrix[source_node - 1][i]})

    visited_nodes_set = {source_node}  # Source is already visited.
    while True:
        closest_dist, closest_node = find_closest_unvisited_node(shortest_paths_dict, visited_nodes_set)
        shortest_paths_dict.update({closest_node: closest_dist})  # The closest unvisited node to source.

        for node in shortest_paths_dict.keys():  # Update distances from min node to other nodes.
            if adjacency_matrix[closest_node - 1][node - 1] + closest_dist < shortest_paths_dict[node]:
                shortest_paths_dict.update({node: adjacency_matrix[closest_node - 1][node - 1] + closest_dist})

        visited_nodes_set.add(closest_node)  # Now this closest unvisited node becomes visited.
        if len(visited_nodes_set) == len(adjacency_matrix):  # Break whenever all nodes are visited.
            break

    del visited_nodes_set, source_node, adjacency_matrix
    return shortest_paths_dict


if __name__ == '__main__':
    source, destinations_list, distances_str = 1, [7, 37, 59, 82, 99, 115, 133, 165, 188, 197], ''
    shortest_paths_dictionary = find_shortest_path(process_distances(), source)

    if len(shortest_paths_dictionary) > 0:
        for destination in destinations_list:
            distances_str += str(shortest_paths_dictionary[destination])
            if destinations_list[-1] != destination:
                distances_str += ','

    print(f'Distances from {source} to each of {destinations_list}:\n{distances_str}')
