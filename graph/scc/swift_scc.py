from graph.scc.utils.graph_reducer import shrink_graph
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from copy import deepcopy


class SuperSwiftSearch:
    """Super swift strongly-connected components search."""

    def __init__(self, edges_dict: dict):
        self.edges_dict, self.one_sided_set, self.closed_pairs_set = shrink_graph(edges_dict)

        # One-sided nodes and closed pairs are finalized SCC and can be stored directly.
        self.scc_dict, self.scc_order = dict(), 1
        for node in self.one_sided_set:
            self.scc_dict.update({self.scc_order: [node]})
            self.scc_order += 1

        for closed_pair in self.closed_pairs_set:
            self.scc_dict.update({self.scc_order: [closed_pair[0], closed_pair[-1]]})
            self.scc_order += 1

    def search_scc(self):
        if len(self.edges_dict) <= 0:
            return self.scc_dict  # Early return if edges dict is empty.

        pending_nodes_set = set(self.edges_dict.keys())
        pending_nodes_set.update(set(sum(self.edges_dict.values(), [])))

        pending_mapping_dict = dict(zip(pending_nodes_set, range(len(pending_nodes_set))))
        pending_reversed_mapping_dict = dict(zip(range(len(pending_nodes_set)), pending_nodes_set))

        pending_count = len(pending_mapping_dict)
        pending_matrix = [[0 for _ in range(pending_count)] for _ in range(pending_count)]

        for out_node in self.edges_dict.keys():
            out_idx = pending_mapping_dict[out_node]
            in_idx_list = [pending_mapping_dict[in_node] for in_node in self.edges_dict[out_node]]

            for in_idx in in_idx_list:
                pending_matrix[out_idx][in_idx] = 1

        pending_graph = csr_matrix(pending_matrix)
        scc_labels = connected_components(csgraph=pending_graph, connection='strong')[1]  # Only need labels.

        scc_list = []
        for label in range(len(scc_labels)):
            scc_list.extend([pending_reversed_mapping_dict[idx] for idx, val in enumerate(scc_labels) if val == label])
            self.scc_dict.update({self.scc_order: deepcopy(scc_list)})
            scc_list.clear()
            self.scc_order += 1

        del pending_mapping_dict, pending_reversed_mapping_dict, pending_graph, scc_labels, scc_list
        return self.scc_dict


if __name__ == '__main__':
    from graph.scc.utils.graph_reader import read_graph
    import time

    start_time = time.time()
    edges_dictionary = read_graph()
    super_swift = SuperSwiftSearch(edges_dictionary)

    # Rank by descending SCC size.
    scc_dict = dict(sorted(super_swift.search_scc().items(), key=lambda item: len(item[1]), reverse=True))
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
