from config import DATA_FOLDER_PATH
import os
from itertools import chain


class KruskalClustering:
    """Cluster points via Kruskal's algorithm."""

    def __init__(self, edges_dict: dict = None):  # Dict format: key = (node 1, node 2), value = edge length.
        if edges_dict is None:
            edges_dict = self.read_nodes()
        self.clusters_dict, self.edges_dict = dict(), edges_dict
        self.dist_list = list(self.edges_dict.values())
        self.nodes_list = list(set(chain(*list(edges_dict.keys()))))
        self.nodes_list.sort()

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

    def cluster(self, clusters_num: int, max_space_only=True):
        if clusters_num < 1 or clusters_num > len(self.nodes_list):
            raise ValueError('Number of clusters should >= 1 and <= total nodes.')

        if clusters_num == 1:
            self.clusters_dict.update({'1': list(self.nodes_list)})

        if clusters_num == len(self.nodes_list):
            self.clusters_dict = dict(zip([str(i + 1) for i in range(len(self.nodes_list))], self.nodes_list))

        while True:
            if len(self.clusters_dict) == clusters_num:
                break

        if max_space_only:
            return max(self.dist_list)
        return max(self.dist_list), self.clusters_dict


if __name__ == '__main__':
    import time

    start_time = time.time()
    edges_dictionary = {('1', '2'): 5, ('1', '3'): 8, ('1', '4'): 3, ('2', '3'): 6, ('2', '4'): 2, ('3', '4'): 7}
    kruskal_clustering = KruskalClustering(edges_dictionary)
    print(kruskal_clustering.cluster(1, False))

    end_time = time.time()
    print(f'Run Time: {str(round(end_time - start_time))} seconds.')
