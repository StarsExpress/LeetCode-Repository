from itertools import chain


def remove_one_sided_nodes(edges_dict: dict):  # Graph is stored in a format of edges dict.
    out_nodes_set = set(edges_dict.keys())  # Nodes with outgoing edges.
    # Outgoing nodes' incoming edges are in list format.
    in_nodes_set = set(chain.from_iterable(edges_dict.values()))  # Nodes with incoming edges.

    # If SCC has size > 1, all of its nodes have "both outgoing and incoming" edges.
    # From edges dict, find all the nodes with only one of outgoing and incoming edges.
    # Remove these "one-side" nodes from edges dict's keys and values reference.
    one_sided_nodes_set = set()

    while True:
        in_only_nodes_set = in_nodes_set - out_nodes_set  # Nodes with only incoming edges.
        out_only_nodes_set = out_nodes_set - in_nodes_set  # Nodes with only outgoing edges.

        # Some nodes may become one-sided in current iteration.
        iter_one_sided_nodes_set = in_only_nodes_set.union(out_only_nodes_set)
        one_sided_nodes_set = one_sided_nodes_set.union(iter_one_sided_nodes_set)

        if (len(out_nodes_set) <= 0) or (out_nodes_set == in_nodes_set):
            del in_only_nodes_set, out_only_nodes_set, iter_one_sided_nodes_set
            break  # One-sided nodes are all removed if outgoing-only set is empty or equals incoming-only set.

        for only_out_node in out_only_nodes_set:  # Delete keys reference.
            del edges_dict[only_out_node]

        for key, value in edges_dict.items():  # Delete values reference.
            if set(value).intersection(iter_one_sided_nodes_set) == set():
                continue

            new_value = list(set(value) - iter_one_sided_nodes_set)
            edges_dict[key].clear()
            edges_dict[key].extend(new_value)

        empty_nodes_set = set(filter(lambda x: len(edges_dict[x]) <= 0, edges_dict.keys()))
        for empty_node in empty_nodes_set:  # In edges dict, delete nodes that have empty edges list.
            del edges_dict[empty_node]
            one_sided_nodes_set.add(empty_node)  # Record such nodes to one-sided notes set.

        out_nodes_set = set(edges_dict.keys())  # Update for next iteration.
        in_nodes_set = set(chain.from_iterable(edges_dict.values()))

    del out_nodes_set, in_nodes_set
    return edges_dict, one_sided_nodes_set  # Now all nodes in edges dict have both outgoing and incoming edges.


def remove_closed_pairs(edges_dict: dict):  # Graph is stored in a format of edges dict.
    # Two nodes are a closed pair if their outgoing edges only go to each other.

    pairs_set = set()  # Store "tuples" of nodes that are closed pairs to each other. One of function's output.
    pairs_nodes_set = set()  # Store "nodes" that belong to pairs.

    # Nodes that have only one outgoing edge.
    one_out_nodes_set = set(filter(lambda x: len(edges_dict[x]) == 1, edges_dict.keys()))

    for out_node in one_out_nodes_set:
        receiving_node = edges_dict[out_node][0]
        if (receiving_node in one_out_nodes_set) and (edges_dict[receiving_node][0] == out_node):
            pairs_nodes_set.add(out_node)
            pairs_nodes_set.add(receiving_node)

            pairs_set.add((min(out_node, receiving_node), max(out_node, receiving_node)))

    for closed_node in pairs_nodes_set:  # Delete keys reference.
        del edges_dict[closed_node]

    for key, value in edges_dict.items():  # Delete values reference.
        if set(value).intersection(pairs_nodes_set) == set():
            continue

        new_value = list(set(value) - pairs_nodes_set)
        edges_dict[key].clear()
        edges_dict[key].extend(new_value)

    one_sided_nodes_set = set(filter(lambda x: len(edges_dict[x]) <= 0, edges_dict.keys()))
    for one_sided_node in one_sided_nodes_set:  # In edges dict, delete nodes that have empty edges list.
        del edges_dict[one_sided_node]

    del one_out_nodes_set, pairs_nodes_set
    return edges_dict, one_sided_nodes_set, pairs_set
