from graph.scc.utils.nodes_removal import remove_one_sided_nodes, remove_closed_pairs


def shrink_graph(edges_dict: dict):  # Graph is stored in a format of edges dict.
    one_sided_nodes_set, closed_pairs_set = set(), set()
    while True:
        edges_dict_len = len(edges_dict)  # Update for comparison.

        # Remove one-sided nodes first.
        edges_dict, iter_one_sided_nodes_set = remove_one_sided_nodes(edges_dict)
        one_sided_nodes_set.update(iter_one_sided_nodes_set)

        # Then remove closed pairs.
        edges_dict, iter_one_sided_nodes_set, iter_closed_pairs_set = remove_closed_pairs(edges_dict)
        one_sided_nodes_set.update(iter_one_sided_nodes_set)
        closed_pairs_set.update(iter_closed_pairs_set)

        if len(edges_dict) == edges_dict_len:
            break  # Graph converges if edges don't decrease after removal of one-sided nodes and closed pairs.

    del edges_dict_len
    return edges_dict, one_sided_nodes_set, closed_pairs_set
