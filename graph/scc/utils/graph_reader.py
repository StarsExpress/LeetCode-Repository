from config import DATA_FOLDER_PATH
import os


def read_graph():
    file_path = os.path.join(DATA_FOLDER_PATH, 'edges', 'edges_1m.txt')
    with open(file_path, 'r') as file:
        nodes = file.read().splitlines()
        file.close()

    edges_dict = dict()
    for node in nodes:
        nodes_list = node.lstrip().rstrip().split(' ')  # Remove boundary spaces and split by middle space.
        if nodes_list[0] == nodes_list[1]:
            continue  # Ignore self edges.

        if nodes_list[0] not in edges_dict.keys():  # Edges dict: edges from 1st node to 2nd node.
            edges_dict.update({nodes_list[0]: list()})
        if nodes_list[1] not in edges_dict[nodes_list[0]]:  # Prevent duplicated edges.
            edges_dict[nodes_list[0]].append(nodes_list[1])

    del file, file_path, node, nodes, nodes_list
    return edges_dict
