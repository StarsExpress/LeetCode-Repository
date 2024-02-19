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

    def __init__(self, edges_dict):
        # Edges dict stores graph and reversed dict stores reversed graph.
        self.edges_dict, self.reversed_dict = edges_dict, dict()
        self.topology_dict, self.scc_dict = dict(), dict()  # Topology dict keys: orders; values: nodes.

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

    def sort_topology(self, pivot_node=None, return_topology=False):  # Sort topology on graph.
        if pivot_node is None:  # Pending nodes: graph's edges that haven't done topology.
            pending_nodes_list = list(set(self.edges_dict.keys()) - set(self.topology_dict.values()))
            if len(pending_nodes_list) <= 0:
                return self.topology_dict
            pivot_node = random.choice(pending_nodes_list)

        if (len(self.edges_dict) <= 0) | (pivot_node not in self.edges_dict.keys()):
            return self.topology_dict  # Early return for these two unreasonable cases.

        outgoing_nodes_set = set(self.edges_dict.keys())  # Outgoing nodes in original graph.
        topology_order = max(self.topology_dict.keys()) + 1 if len(self.topology_dict) > 0 else 1
        stack_list = [pivot_node]  # Stack always starts with pivot.

        while True:
            # Visited nodes: either complete topology or are in stack.
            visited_nodes_set = set(self.topology_dict.values()).union(set(stack_list))

            # Pivot completes topology if it's a sink node or only walks to visited nodes.
            if pivot_node not in outgoing_nodes_set or set(self.edges_dict[pivot_node]).issubset(visited_nodes_set):
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

        del outgoing_nodes_set, stack_list, visited_nodes_set, pending_nodes_list, pivot_node, topology_order

        if return_topology:
            return self.topology_dict

    def search_scc(self, return_scc=False):  # Search SCC on reversed graph.
        if len(self.edges_dict) <= 0:
            return self.scc_dict  # Early return if edges dict is empty.
        if len(self.topology_dict) <= 0:
            self.sort_topology()  # Ensure edges dict has been through topology.
        if len(self.reversed_dict) <= 0:
            self.reverse_edges()  # Ensure a reversed version of edges dict.

        outgoing_nodes_set = set(self.reversed_dict.keys())  # Outgoing nodes in reversed graph.
        scc_ordinal = 1  # SCC ordinal starts from 1.

        pivot_node = self.topology_dict[max(self.topology_dict.keys())]  # Start from the highest-ordered node.

        # Current SCC dict stores all nodes related to "current" SCC search.
        # Unblocked: a node that either isn't sink node or hasn't reached nodes from current or "past" SCC search.
        # Blocked: the opposite of an unblocked node.
        # Just as stack, unblocked list always starts with pivot.
        current_scc_dict = {'unblocked': [pivot_node], 'blocked': []}

        topology_orders_list = list(self.topology_dict.keys())

        while True:
            # All SCC set: set of nodes from current or past SCC search.
            all_scc_set = set(sum(current_scc_dict.values(), [])).union(set(sum(self.scc_dict.values(), [])))

            # If a pivot is blocked.
            if pivot_node not in outgoing_nodes_set or set(self.reversed_dict[pivot_node]).issubset(all_scc_set):
                current_scc_dict['blocked'].append(pivot_node)  # Move pivot from unblocked into blocked list.
                current_scc_dict['unblocked'].remove(pivot_node)

            # Add unblocked pivot's unblocked children into unblocked list.
            if pivot_node in current_scc_dict['unblocked']:
                for pivot_node_child in self.reversed_dict[pivot_node]:
                    if pivot_node_child not in all_scc_set:
                        current_scc_dict['unblocked'].append(pivot_node_child)

            # If unblocked pivot has no unblocked children, current SCC search is completed in either cases.
            if len(current_scc_dict['unblocked']) <= 1:
                self.scc_dict.update({str(scc_ordinal): current_scc_dict['unblocked'] + current_scc_dict['blocked']})
                scc_ordinal += 1  # Increment for the next round of SCC search.

                # Only break while if all nodes have done SCC search.
                if set(self.reversed_dict.keys()) - set(sum(self.scc_dict.values(), [])) == set():
                    break

                # Remove current SCC nodes' orders from list.
                for current_scc_node in current_scc_dict['unblocked'] + current_scc_dict['blocked']:
                    current_scc_index = list(self.topology_dict.values()).index(current_scc_node)
                    topology_orders_list.remove(list(self.topology_dict.keys())[current_scc_index])

                current_scc_dict['unblocked'].clear()
                current_scc_dict['blocked'].clear()

                pivot_node = self.topology_dict[max(topology_orders_list)]
                current_scc_dict['unblocked'].append(pivot_node)

            pivot_node = current_scc_dict['unblocked'][-1]  # Follow DFS stack rule: last in first out.

        del outgoing_nodes_set, current_scc_dict, all_scc_set, scc_ordinal, pivot_node
        if return_scc:
            return self.scc_dict


if __name__ == '__main__':
    # edges_dictionary = process_edges()
    edges_dictionary = {'0': {'1'}, '1': ['2', '4'], '2': ['0', '3'], '3': ['2'],
                        '4': ['5', '6'], '5': ['4', '6', '7'],
                        '6': ['7'], '7': ['8'], '8': ['6']}
    dfs = DepthFirstSearch(edges_dictionary)
    # Rank by descending SCC size.
    scc_dict = dict(sorted(dfs.search_scc(return_scc=True).items(), key=lambda item: len(item[1]), reverse=True))

    top_5_scc_size_string = 'Top 5 SCC Size: '
    for i in range(5):
        if i + 1 > len(scc_dict):
            top_5_scc_size_string += '0'

        else:
            top_5_scc_size_string += f'{len(list(scc_dict.values())[i])}'

        if i == 4:
            break
        top_5_scc_size_string += ','
    print(top_5_scc_size_string)
