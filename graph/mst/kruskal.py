from config import DATA_FOLDER_PATH
import os
from itertools import chain


class KruskalMST:
    """Find MST via Kruskal's algorithm."""

    def __init__(self, edges_dict: dict = None):  # Dict format: key = (node 1, node 2), value = edge length.
        if edges_dict is None:
            edges_dict = self.read_nodes()
        self.edges_dict = edges_dict

        all_nodes_set = set(chain(*list(edges_dict.keys())))
        self.roots_dict = dict(zip(all_nodes_set, [None] * len(all_nodes_set)))  # Each node's root in MST.
        del all_nodes_set

    @staticmethod
    def read_nodes():
        file_path = os.path.join(DATA_FOLDER_PATH, 'nodes_500.txt')
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

    def union(self, node_1: str, node_2: str):
        root_1, root_2 = self.find(node_1), self.find(node_2)
        if root_1 is None and root_2 is None:  # If both nodes aren't in MST yet.
            self.roots_dict.update({node_1: node_1})
            self.roots_dict.update({node_2: node_1})
            return

        if root_1 is None and root_2 is not None:  # If node 1 isn't in but node 2 is.
            self.roots_dict.update({node_1: root_2})
            return

        if root_1 is not None and root_2 is None:  # If node 2 isn't in but node 1 is.
            self.roots_dict.update({node_2: root_1})
            return

        self.roots_dict.update({root_2: root_1})  # If both are in, union one's set to the other's set.

    def find(self, node: str):  # Find a node's root in MST.
        if self.roots_dict[node] is None:  # If a node isn't in MST yet.
            return None

        if self.roots_dict[node] != node:  # If a node's root isn't itself, trace upward till the end.
            self.roots_dict.update({node: self.find(self.roots_dict[node])})
        return self.roots_dict[node]

    def seek_mst(self, distance_only=False):
        mst_dict = dict()
        edges_dict = dict(sorted(self.edges_dict.items(), key=lambda item: item[1]))  # Sort by ascending edge distance.
        edges_list, edges_idx = list(edges_dict.keys()), 0  # Edges list: list of tuples of connected nodes.

        while True:
            node_1, node_2 = edges_list[edges_idx]
            root_1, root_2 = self.find(node_1), self.find(node_2)

            edges_idx += 1  # Increment index once roots of nodes are found.
            if (root_1 is not None) and (root_1 == root_2):
                continue  # If current edge causes cycle, skip this edge.

            # Use nodes tuple to call dict, as edges idx has incremented.
            mst_dict.update({(node_1, node_2): edges_dict[(node_1, node_2)]})
            if len(mst_dict) == len(self.roots_dict) - 1:  # MST needs n - 1 edges; n = total nodes.
                break
            self.union(node_1, node_2)

        del edges_dict, node_1, node_2, edges_idx, edges_list
        if distance_only:
            return sum(mst_dict.values())
        return mst_dict, sum(mst_dict.values())


if __name__ == '__main__':
    import time

    start_time = time.time()
    kruskal_mst = KruskalMST()
    print(kruskal_mst.seek_mst(True))

    end_time = time.time()
    print(f'Run Time: {str(round(end_time - start_time))} seconds.')
