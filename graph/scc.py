from graph.scc_utils.convergence import converge_graph
import random
from copy import deepcopy


class KosarajuSearch:
    """Search strongly-connected components via Kosaraju algorithm."""

    def __init__(self, edges_dict: dict):
        self.edges_dict, self.one_sided_set, self.closed_pairs_set = converge_graph(edges_dict)
        self.reversed_dict = dict()  # Stores reversed graph.
        self.all_nodes_set = set(self.edges_dict.keys())  # All nodes of "converged" graph.

        self.topology_dict = dict()  # Topology dict keys: orders; values: nodes.
        self.stack_list, self.topology_order = [], 1  # Initially, stack is empty and topology order is 1.

        # One-sided nodes and closed pairs are finalized SCC and can be stored directly.
        self.scc_dict = dict(zip(range(1, len(self.one_sided_set) + 1), [[node] for node in self.one_sided_set]))
        for closed_pair in self.closed_pairs_set:
            self.scc_dict.update({len(self.scc_dict) + 1: [closed_pair[0], closed_pair[-1]]})
        self.scc_order = len(self.scc_dict) + 1

        # Used during SCC search: list of topology orders; list of current SCC components;.set of nodes from past SCC.
        self.topology_orders_list, self.current_scc_list, self.scc_nodes_set = [], [], set()

        self.pending_nodes_list = list(self.all_nodes_set)  # Initially, all nodes haven't done topology.
        self.visited_nodes_set = set()  # Visited nodes: either complete topology or are in stack.

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
        self.scc_nodes_set.update(set(self.current_scc_list))

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
    from graph.scc_utils.reader import read_graph
    import time

    start_time = time.time()
    edges_dictionary = read_graph()
    kosaraju = KosarajuSearch(edges_dictionary)

    # Rank by descending SCC size.
    scc_dict = dict(sorted(kosaraju.search_scc().items(), key=lambda item: len(item[1]), reverse=True))
    top_5_scc_size_string = 'Top 5 SCC Size: '
    for i in range(5):
        if i + 1 > len(scc_dict):
            top_5_scc_size_string += '0'

        else:
            top_5_scc_size_string += f'{len(list(scc_dict.values())[i])}'

        if i == 4:
            break
        top_5_scc_size_string += ','

    end_time = time.time()
    print(f'{top_5_scc_size_string}\nRun Time: {str(round(end_time - start_time))} seconds.')
