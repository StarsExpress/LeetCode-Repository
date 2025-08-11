
def count_valid_triangles(edges: list[int]) -> int:  # LeetCode Q.611.
    edges.sort()
    total_triangles, total_edges = 0, len(edges)

    for edge_3_idx in range(total_edges - 1, -1, -1):
        edge_1_idx, edge_2_idx = 0, edge_3_idx - 1

        while edge_1_idx < edge_2_idx:
            if edges[edge_1_idx] + edges[edge_2_idx] > edges[edge_3_idx]:
                total_triangles += edge_2_idx - edge_1_idx
                edge_2_idx -= 1

            else:
                edge_1_idx += 1

    return total_triangles
