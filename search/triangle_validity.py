
def count_valid_3rd_edges(two_edges_sum, sorted_edges: list | tuple):
    if len(sorted_edges) <= 0:
        return 0

    back_idx, front_idx = 0, len(sorted_edges) - 1
    while True:
        if back_idx > front_idx:
            return back_idx  # Implies number of 3rd edges < sum of two input edges.

        mid_idx = back_idx + (front_idx - back_idx) // 2
        if sorted_edges[mid_idx] < two_edges_sum:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def count_valid_triangles(edges: list[int]):  # LeetCode Q.611.
    if len(edges) < 3:
        return 0

    count, back_idx, front_idx = 0, 0, 1
    edges.sort()  # From smallest to biggest.
    while True:
        if front_idx + 1 >= len(edges):
            if back_idx >= front_idx - 1:
                return count

            back_idx += 1
            front_idx = back_idx + 1
            continue

        two_edges_sum = edges[back_idx] + edges[front_idx]
        if two_edges_sum > edges[front_idx + 1]:
            count += count_valid_3rd_edges(two_edges_sum, edges[front_idx + 1:])
        front_idx += 1
