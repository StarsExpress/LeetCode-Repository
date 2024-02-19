from config import DATA_FOLDER_PATH
import os
import random


def process_edges():
    file_path = os.path.join(DATA_FOLDER_PATH, 'directed_edges.txt')
    with open(file_path, 'r') as file:
        nodes = file.read().splitlines()
        file.close()

    edges_dict = dict()
    for node in nodes:
        nodes_list = node.lstrip().rstrip().split(' ')  # Remove boundary spaces and split by middle space.

        if nodes_list[0] not in edges_dict.keys():  # Edges dict: edges from 1st node to 2nd node.
            edges_dict.update({nodes_list[0]: list()})
        if nodes_list[1] not in edges_dict[nodes_list[0]]:  # Prevent duplicated edges.
            edges_dict[nodes_list[0]].append(nodes_list[1])

    del file, file_path, node, nodes, nodes_list
    return edges_dict


class DepthFirstSearch:
    """Depth first search and strongly-connected components search."""

    def __init__(self, edges_dict):  # Topology dict keys: orders; values: nodes.
        self.edges_dict, self.reversed_dict, self.topology_dict, self.scc_dict = edges_dict, dict(), dict(), dict()

    def reverse_edges(self, return_dict=False):  # For each edge, reverse incoming node and outgoing node.
        for outgoing_node in self.edges_dict.keys():
            incoming_nodes_list = self.edges_dict[outgoing_node]
            for incoming_node in incoming_nodes_list:
                if incoming_node not in self.reversed_dict.keys():
                    self.reversed_dict.update({incoming_node: list()})
                self.reversed_dict[incoming_node].append(outgoing_node)

        del outgoing_node, incoming_node, incoming_nodes_list
        if return_dict:
            return self.reversed_dict

    def sort_topology(self, pivot_node=None, return_topology=False):
        if pivot_node is None:  # Pending nodes: in edges dict but haven't done topology.
            pending_nodes_list = list(set(self.edges_dict.keys()) - set(self.topology_dict.values()))
            if len(pending_nodes_list) <= 0:
                return self.topology_dict
            pivot_node = random.choice(pending_nodes_list)

        if (len(self.edges_dict) <= 0) | (pivot_node not in self.edges_dict.keys()):
            return self.topology_dict  # Return topology dict for these two unreasonable cases.

        topology_order = max(self.topology_dict.keys()) + 1 if len(self.topology_dict) > 0 else 1
        stack_list = [pivot_node]  # Stack always starts with pivot.
        outgoing_nodes_list = list(set(self.edges_dict.keys()))  # Nodes with outgoing edge(s).

        while True:
            # Visited nodes: either complete topology or are in stack.
            visited_nodes_set = set(self.topology_dict.values()).union(set(stack_list))

            # Pivot completes topology if it's a sink node or only walks to visited nodes.
            if pivot_node not in outgoing_nodes_list or set(self.edges_dict[pivot_node]).issubset(visited_nodes_set):
                self.topology_dict.update({topology_order: pivot_node})
                topology_order += 1  # Increment for the next topology completion.
                stack_list.remove(pivot_node)  # Leave stack.

            if len(stack_list) <= 0:  # When stack is empty, check if there are pending nodes.
                pending_nodes_list = list(set(self.edges_dict.keys()) - set(self.topology_dict.values()))
                if len(pending_nodes_list) <= 0:  # Only break while if all nodes have done topology.
                    break

                pivot_node = random.choice(pending_nodes_list)
                stack_list.append(pivot_node)

            if pivot_node in stack_list:  # If pivot is in stack, add its unvisited children into stack.
                for pivot_node_child in self.edges_dict[pivot_node]:
                    if pivot_node_child not in visited_nodes_set:
                        stack_list.append(pivot_node_child)

            pivot_node = stack_list[-1]  # DFS stack rule: last in first out.

        del outgoing_nodes_list, stack_list, visited_nodes_set, pending_nodes_list
        del pivot_node, pivot_node_child, topology_order
        self.topology_dict = dict(sorted(self.topology_dict.items(), key=lambda item: item[0], reverse=True))

        if return_topology:
            return self.topology_dict  # Return dict sorted by descending topology orders.


if __name__ == '__main__':
    # edges_dictionary = process_edges()
    edges_dictionary = {'0': {'1'}, '1': ['2', '4'], '2': ['0', '3'], '3': ['2'],
                        '4': ['5', '6'], '5': ['4', '6', '7'],
                        '6': ['7'], '7': ['8'], '8': ['6']}
    dfs = DepthFirstSearch(edges_dictionary)
    print(dfs.sort_topology(return_topology=True))
