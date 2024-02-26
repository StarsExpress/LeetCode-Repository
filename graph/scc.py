from config import DATA_FOLDER_PATH
import os
from itertools import chain
import random
from copy import deepcopy


def read_graph():
    file_path = os.path.join(DATA_FOLDER_PATH, 'edges_1m.txt')
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


class KosarajuSearch:
    """Search strongly-connected components via Kosaraju algorithm."""

    def __init__(self, edges_dict: dict):
        self.edges_dict, self.one_sided_nodes_set = self.remove_one_sided_nodes(edges_dict)
        self.reversed_dict = dict()  # Stores reversed graph.
        self.all_nodes_set = set(self.edges_dict.keys())  # All nodes of graph.

        self.topology_dict, self.scc_dict = dict(), dict()  # Topology dict keys: orders; values: nodes.
        # At initialization, stack is empty and two orders are both 1.
        self.stack_list, self.topology_order, self.scc_order = [], 1, 1

        # Used during SCC search: list of topology orders; list of current SCC components;.set of nodes from past SCC.
        self.topology_orders_list, self.current_scc_list, self.scc_nodes_set = [], [], set()

        self.pending_nodes_list = list(self.all_nodes_set)  # Initially, all nodes haven't done topology.
        self.visited_nodes_set = set()  # Visited nodes: either complete topology or are in stack.

    @staticmethod
    def remove_one_sided_nodes(edges_dict: dict):  # Graph is stored in a format of edges dict.
        out_nodes_set = set(edges_dict.keys())  # Nodes with outgoing edges.
        # Outgoing nodes' incoming edges are in list format.
        in_nodes_set = set(chain.from_iterable(edges_dict.values()))  # Nodes with incoming edges.

        # If SCC has size > 1, all of its nodes have "both outgoing and incoming" edges.
        # From edges dict, find all the nodes with only one of outgoing and incoming edges.
        # Remove these "one-side" nodes from edges dict's keys and values reference.
        one_sided_nodes_set = set()

        while True:
            only_in_nodes_set = in_nodes_set - out_nodes_set  # Nodes with only incoming edges.
            only_out_nodes_set = out_nodes_set - in_nodes_set  # Nodes with only outgoing edges.

            # Some nodes may become one-sided in current iteration.
            iter_one_sided_nodes_set = only_in_nodes_set.union(only_out_nodes_set)
            one_sided_nodes_set = one_sided_nodes_set.union(iter_one_sided_nodes_set)

            if (len(out_nodes_set) <= 0) or (out_nodes_set == in_nodes_set):
                del only_in_nodes_set, only_out_nodes_set, iter_one_sided_nodes_set
                break  # Graph converges if outgoing nodes set is empty or equals incoming nodes set.

            for only_out_node in only_out_nodes_set:  # Delete keys reference.
                del edges_dict[only_out_node]

            for key, value in edges_dict.items():  # Delete values reference.
                if set(value).intersection(iter_one_sided_nodes_set) == set():
                    continue

                new_value = list(set(value) - iter_one_sided_nodes_set)
                edges_dict[key].clear()
                edges_dict[key].extend(new_value)

            out_nodes_set = set(edges_dict.keys())  # Update for next iteration.
            in_nodes_set = set(chain.from_iterable(edges_dict.values()))

        del out_nodes_set, in_nodes_set
        return edges_dict, one_sided_nodes_set  # Now all nodes in edges dict have both outgoing and incoming edges.

    @staticmethod
    def remove_closed_pairs(edges_dict: dict):
        closed_pairs_set = set()  # Two nodes are a closed pair if their outgoing edges only go to each other.
        # Nodes that have only one outgoing edge.
        one_out_nodes_set = set(filter(lambda x: len(edges_dict[x]) == 1, edges_dict.keys()))

        for out_node in one_out_nodes_set:
            receiving_node = edges_dict[out_node][0]
            if (receiving_node in one_out_nodes_set) and (edges_dict[receiving_node][0] == out_node):
                closed_pairs_set.add(out_node)
                closed_pairs_set.add(receiving_node)

        print(len(closed_pairs_set))

    def reverse_edges(self, return_dict=False):  # For each edge, reverse incoming node and outgoing node.
        for out_node in self.edges_dict.keys():
            in_nodes_list = self.edges_dict[out_node]
            for in_node in in_nodes_list:
                if in_node not in self.reversed_dict.keys():
                    self.reversed_dict.update({in_node: list()})
                self.reversed_dict[in_node].append(out_node)

        del out_node, in_node, in_nodes_list
        if return_dict:
            return self.reversed_dict

    def sort_topology(self):
        if len(self.stack_list) <= 0:  # If stack is empty, randomly choose a node that hasn't done topology.
            if len(self.pending_nodes_list) <= 0:
                return
            start_node = random.choice(self.pending_nodes_list)
            self.stack_list.append(start_node)
            self.visited_nodes_set.add(start_node)

        start_node = self.stack_list[-1]  # Start node is the last item in stack. DFS stack rule: last in first out.

        original_stack_count = len(self.stack_list)
        if start_node in self.edges_dict.keys():  # Add unvisited children of start node to stack.
            for child in self.edges_dict[start_node]:
                if child not in self.visited_nodes_set:
                    self.stack_list.append(child)
                    self.visited_nodes_set.add(child)

        # Start node completes topology if it's a "sink" node or only walks to visited children.
        if len(self.stack_list) == original_stack_count:
            self.topology_dict.update({self.topology_order: start_node})
            self.stack_list.remove(start_node)  # Leave stack.
            self.pending_nodes_list.remove(start_node)
            self.topology_order += 1  # Increment for the next node that completes topology.

            if len(self.stack_list) <= 0:  # When stack is empty, check if there are pending nodes.
                if len(self.pending_nodes_list) <= 0:  # If all nodes have done topology.
                    self.topology_order -= (self.topology_order - 1)  # Topology order is back to 1.

                    # Prepare lists that have to be used in search SCC function.
                    self.topology_orders_list.clear()
                    self.topology_orders_list.extend(sorted(self.topology_dict.keys()))  # Sort from low to high.
                    self.current_scc_list.clear()
                    self.pending_nodes_list.extend(self.all_nodes_set)
                    return  # Return as graph topology completes.

                start_node = random.choice(self.pending_nodes_list)
                self.stack_list.append(start_node)  # Added a new start node to stack.
                self.visited_nodes_set.add(start_node)
        self.sort_topology()

    def search_scc(self):  # Search SCC on reversed graph.
        if len(self.edges_dict) <= 0:
            return self.scc_dict  # Early return if edges dict is empty.
        if len(self.topology_dict) <= 0:
            self.sort_topology()  # Ensure edges dict has been through topology.
        if len(self.reversed_dict) <= 0:
            self.reverse_edges()  # Ensure a reversed version of edges dict.

        if len(self.stack_list) <= 0:
            if len(self.topology_orders_list) <= 0:
                return self.scc_dict

            # Add the node that has the biggest topology order of topology orders list.
            biggest_order_node = self.topology_dict[max(self.topology_orders_list)]
            self.stack_list.append(biggest_order_node)

        start_node = self.stack_list[-1]  # Start node is the last item in stack. DFS stack rule: last in first out.
        self.scc_nodes_set.update(set(self.stack_list))
        self.scc_nodes_set.union(set(self.current_scc_list))

        original_stack_count = len(self.stack_list)
        if start_node in self.reversed_dict.keys():  # Add unvisited children of start node to stack.
            for child in self.reversed_dict[start_node]:
                if child not in self.scc_nodes_set:
                    self.stack_list.append(child)

        # Start node reaches end if it's a "sink" node or only walks to visited children.
        if len(self.stack_list) == original_stack_count:
            self.current_scc_list.append(start_node)  # Move start node from stack to current SCC list.
            self.stack_list.remove(start_node)

            if len(self.stack_list) <= 0:  # When stack is empty, current SCC search is complete.
                # Update current SCC components into SCC dict and set.
                self.scc_dict.update({self.scc_order: deepcopy(self.current_scc_list)})  # Deep copy to prevent bugs.
                self.current_scc_list.clear()  # Clear list after updates are finished.

                # In current SCC search, all N components have the N biggest topology orders. Remove them from list.
                for _ in range(len(self.scc_dict[self.scc_order])):
                    self.topology_orders_list.remove(self.topology_orders_list[-1])

                if len(self.topology_orders_list) <= 0:  # If all graph nodes have done SCC search.
                    self.scc_order -= (self.scc_order - 1)  # SCC order is back to 1.

                    self.topology_orders_list.clear()  # Restore topology orders. Sort from low to high.
                    self.topology_orders_list.extend(sorted(self.topology_dict.keys()))
                    return self.scc_dict  # Return as SCC search completes.

                self.scc_order += 1  # Increment SCC order for the next round of SCC search.

        self.search_scc()
        return self.scc_dict


if __name__ == '__main__':
    import time

    start_time = time.time()
    edges_dictionary = read_graph()
    # edges_dictionary = {'0': ['1'], '1': ['2', '4'], '2': ['0', '3'], '3': ['2'],
    #                     '4': ['5', '6'], '5': ['4', '6', '7'],
    #                     '6': ['7'], '7': ['8'], '8': ['6']}

    kosaraju = KosarajuSearch(edges_dictionary)
    kosaraju.remove_closed_pairs(kosaraju.edges_dict)
    # print(len(kosaraju.edges_dict), len(kosaraju.one_sided_nodes_set))

    # # Rank by descending SCC size.
    # scc_dict = dict(sorted(kosaraju.search_scc().items(), key=lambda item: len(item[1]), reverse=True))
    # top_5_scc_size_string = 'Top 5 SCC Size: '
    # for i in range(5):
    #     if i + 1 > len(scc_dict):
    #         top_5_scc_size_string += '0'
    #
    #     else:
    #         top_5_scc_size_string += f'{len(list(scc_dict.values())[i])}'
    #
    #     if i == 4:
    #         break
    #     top_5_scc_size_string += ','
    #
    # end_time = time.time()
    # print(f'{top_5_scc_size_string}\nRun Time: {str(round(end_time - start_time))} seconds.')
