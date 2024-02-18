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


def do_depth_first_search(edges_dict, pivot_node, process_dict, stack_list, visited_list):
    if (len(edges_dict) <= 0) | (pivot_node not in edges_dict.keys()):
        return process_dict  # Return process dict for these two unreasonable cases.

    outgoing_nodes_list = list(edges_dict.keys())  # Keys are all nodes with outgoing edge(s).

    # If pivot node is a sink node or only walks to visited nodes.
    if pivot_node not in outgoing_nodes_list or set(edges_dict[pivot_node]).issubset(set(visited_list)):
        process_order = max(process_dict.values()) + 1 if len(process_dict) > 0 else 1
        process_dict.update({pivot_node: process_order})
        del process_order

        stack_list.remove(pivot_node)
        visited_list.append(pivot_node)
        return process_dict, stack_list[-1], stack_list, visited_list

    stack_list.extend(edges_dict[pivot_node])
    process_dict, stack_list, visited_list, pivot_node = do_depth_first_search(edges_dict, pivot_node,
                                                                               process_dict, stack_list, visited_list)

    del edges_dict, outgoing_nodes_list
    return process_dict, pivot_node, stack_list, visited_list


if __name__ == '__main__':
    edges_dictionary = {'0': ['1'], '1': ['2', '4'], '2': ['0', '3'], '3': ['2'],
                        '4': ['5', '6'], '5': ['4', '6', '7'],
                        '6': ['7'], '7': ['8'], '8': ['6']}
    starting_node = '4'
    process_dictionary = do_depth_first_search(edges_dictionary, starting_node, dict(),
                                               edges_dictionary[starting_node], [starting_node])[0]
    print(dict(sorted(process_dictionary.items(), key=lambda item: item[1], reverse=True)))
