from config import DATA_FOLDER_PATH
import os


def process_edges():
    file_path = os.path.join(DATA_FOLDER_PATH, 'directed_edges.txt')
    with open(file_path, 'r') as file:
        nodes = file.read().splitlines()
        file.close()

    edges_dict, reversed_edges_dict = dict(), dict()
    for node in nodes:
        nodes_list = node.lstrip().rstrip().split(' ')  # Remove boundary spaces and split by middle space.

        if nodes_list[0] not in edges_dict.keys():  # Edges dict: edges from 1st node to 2nd node.
            edges_dict.update({nodes_list[0]: list()})
        edges_dict[nodes_list[0]].append(nodes_list[1])

        if nodes_list[1] not in reversed_edges_dict.keys():  # Reversed dict: edges from 2nd node to 1st node.
            reversed_edges_dict.update({nodes_list[1]: list()})
        reversed_edges_dict[nodes_list[1]].append(nodes_list[0])

    del file, file_path, node, nodes, nodes_list
    return edges_dict, reversed_edges_dict


class DepthFirstSearch:
    def __init__(self, edges_dict):
        self.edges_dict = edges_dict
        self.topology_dict = dict()  # Record topological orders of each node under DFS.

    def sort_topology(self, pivot_node=None):
        if pivot_node is None:  # Pending nodes: in edges dict but haven't done topology.
            pending_nodes_list = list(set(self.edges_dict.keys()) - set(self.topology_dict.keys()))
            if len(pending_nodes_list) <= 0:
                return self.topology_dict
            pivot_node = pending_nodes_list.pop()

        if (len(self.edges_dict) <= 0) | (pivot_node not in self.edges_dict.keys()):
            return self.topology_dict  # Return topology dict for these two unreasonable cases.

        topology_order = max(self.topology_dict.values()) + 1 if len(self.topology_dict) > 0 else 1
        stack_list = [pivot_node]  # Stack always starts with pivot.
        outgoing_nodes_list = list(set(self.edges_dict.keys()))  # Nodes with outgoing edge(s).

        while True:
            # Visited nodes: either complete topology or are in stack.
            visited_nodes_set = set(self.topology_dict.keys()).union(set(stack_list))

            # Pivot node completes topology if it's a sink node or only walks to visited nodes.
            if pivot_node not in outgoing_nodes_list or set(self.edges_dict[pivot_node]).issubset(visited_nodes_set):
                self.topology_dict.update({pivot_node: topology_order})
                topology_order += 1  # Increment for the next topology completion.
                stack_list.remove(pivot_node)  # Leave stack.

            if len(stack_list) <= 0:  # When stack is empty, check if there are pending nodes.
                pending_nodes_list = list(set(self.edges_dict.keys()) - set(self.topology_dict.keys()))
                if len(pending_nodes_list) <= 0:  # Only break while if all nodes have done topology.
                    break

                pivot_node = pending_nodes_list.pop()
                stack_list.append(pivot_node)

            if pivot_node in stack_list:
                for pivot_node_child in self.edges_dict[pivot_node]:
                    if pivot_node_child not in visited_nodes_set:
                        stack_list.append(pivot_node_child)  # Add pivot node's unvisited children into stack.

            pivot_node = stack_list[-1]  # DFS stack rule: last in first out.

        del outgoing_nodes_list, stack_list, visited_nodes_set, pending_nodes_list
        del pivot_node, pivot_node_child, topology_order
        return self.topology_dict


if __name__ == '__main__':
    edges_dictionary = {'0': {'1'}, '1': ['2', '4'], '2': ['0', '3'], '3': ['2'],
                        '4': ['5', '6'], '5': ['4', '6', '7'],
                        '6': ['7'], '7': ['8'], '8': ['6']}

    dfs = DepthFirstSearch(edges_dictionary)
    topology_dictionary = dfs.sort_topology()
    print(dict(sorted(topology_dictionary.items(), key=lambda item: item[1], reverse=True)))
