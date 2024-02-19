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

        if nodes_list[0] not in edges_dict.keys():  # Edges dict: store edge from 1st node to 2nd node.
            edges_dict.update({nodes_list[0]: list()})
        edges_dict[nodes_list[0]].append(nodes_list[1])

        # Reversed dict: store edge from 2nd node to 1st node.
        if nodes_list[1] not in reversed_edges_dict.keys():
            reversed_edges_dict.update({nodes_list[1]: list()})
        reversed_edges_dict[nodes_list[1]].append(nodes_list[0])

    del file, file_path, node, nodes, nodes_list
    return edges_dict, reversed_edges_dict


class DepthFirstSearch:
    def __init__(self, edges_dict, process_dict=None):
        self.edges_dict = edges_dict
        if process_dict is None:
            self.process_dict = dict()

        else:
            self.process_dict = process_dict

    def execute(self, pivot_node=None):
        if pivot_node is None:  # Select any unprocessed node as pivot.
            unprocessed_nodes_list = list(set(self.edges_dict.keys()) - set(self.process_dict.keys()))
            if len(unprocessed_nodes_list) <= 0:  # If nodes are all processed.
                return self.process_dict
            pivot_node = unprocessed_nodes_list.pop()

        if (len(self.edges_dict) <= 0) | (pivot_node not in self.edges_dict.keys()):
            return self.process_dict  # Return process dict for these two unreasonable cases.

        process_order = max(self.process_dict.values()) + 1 if len(self.process_dict) > 0 else 1
        outgoing_nodes_list = list(set(self.edges_dict.keys()))  # All nodes with outgoing edge(s).
        stack_list = [pivot_node]  # Stack always starts with pivot.

        while True:
            known_nodes_set = set(self.process_dict.keys()).union(set(stack_list))

            # If pivot node is a sink node or only walks to known nodes.
            if pivot_node not in outgoing_nodes_list or set(self.edges_dict[pivot_node]).issubset(known_nodes_set):
                self.process_dict.update({pivot_node: process_order})
                process_order += 1  # Increment after updating pivot node's process order.
                stack_list.remove(pivot_node)  # Pivot node becomes processed and leaves stack.

            if len(stack_list) <= 0:  # When stack is empty, check if there are unprocessed nodes.
                unprocessed_nodes_list = list(set(self.edges_dict.keys()) - set(self.process_dict.keys()))
                if len(unprocessed_nodes_list) <= 0:  # Only if all processed will the while break.
                    break

                pivot_node = unprocessed_nodes_list.pop()  # Otherwise, pick any unprocessed node as new pivot.
                stack_list.append(pivot_node)

            if pivot_node in stack_list:
                for node in self.edges_dict[pivot_node]:
                    if node not in known_nodes_set:  # From pivot node's outgoing edges, add unknown nodes into stack.
                        stack_list.append(node)

            pivot_node = stack_list[-1]  # DFS stack rule: last in first out.

        del pivot_node, process_order, outgoing_nodes_list, stack_list, known_nodes_set, unprocessed_nodes_list, node
        return self.process_dict


if __name__ == '__main__':
    edges_dictionary = {'0': {'1'}, '1': ['2', '4'], '2': ['0', '3'], '3': ['2'],
                        '4': ['5', '6'], '5': ['4', '6', '7'],
                        '6': ['7'], '7': ['8'], '8': ['6']}
    # starting_node = '6'

    dfs = DepthFirstSearch(edges_dictionary)
    process_dictionary = dfs.execute()
    print(dict(sorted(process_dictionary.items(), key=lambda item: item[1], reverse=True)))
