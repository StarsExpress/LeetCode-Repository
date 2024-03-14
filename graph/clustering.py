from config import DATA_FOLDER_PATH
import os
from itertools import chain


class KruskalClustering:
    """Cluster points via Kruskal's algorithm."""

    def __init__(self, edges_dict: dict = None):   # Dict format: key = (node 1, node 2), value = edge length.
        if edges_dict is None:
            edges_dict = self.read_nodes()
        self.edges_dict = edges_dict
        self.edges_list = list(self.edges_dict.values())
        self.edges_list.sort()

    @staticmethod
    def read_nodes():
        file_path = os.path.join(DATA_FOLDER_PATH, 'edges_120k.txt')
        with open(file_path, 'r') as file:
            nodes = file.read().splitlines()[1:]  # Skip the 1st line that isn't related to edge distance.
            file.close()

        edges_dict = dict()
        for node in nodes:
            nodes_list = node.lstrip().rstrip().split(' ')  # Remove boundary spaces and split by middle space.
            if nodes_list[0] == nodes_list[1]:  # 1st & 2nd items: nodes.
                continue  # Ignore self edges.

            # Edge key format: (smaller node, bigger node).
            edge_key = (min(nodes_list[0], nodes_list[1]), max(nodes_list[0], nodes_list[1]))
            if edge_key not in edges_dict.keys():
                edges_dict.update({edge_key: int(nodes_list[-1])})  # 3rd item: distance but in str.

        del file, file_path, node, nodes, nodes_list, edge_key
        return edges_dict


if __name__ == '__main__':
    import time

    start_time = time.time()
    kruskal_clustering = KruskalClustering()
    print(kruskal_clustering.edges_list)
    # print(kruskal_clustering.find_mst(True))

    end_time = time.time()
    print(f'Run Time: {str(round(end_time - start_time))} seconds.')
