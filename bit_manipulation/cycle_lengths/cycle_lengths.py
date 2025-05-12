
def query_cycle_lengths(queries: list[list[int]]) -> list[int]:  # LeetCode Q.2509.
    answers = []
    ancestors = set()  # Track nodes' common ancestors.

    for node_1, node_2 in queries:
        min_node, max_node = min(node_1, node_2), max(node_1, node_2)

        # Exclude "0b" prefix to have real bin len. Real bin len - 1 = level.
        max_node_level = len(bin(max_node)) - 3
        # Exclude "0b" prefix to have real bin len. Real bin len - 1 = level.
        min_node_level = len(bin(min_node)) - 3

        ancestors.add(min_node)  # Min node might be max node's ancestor.
        while min_node > 1:  # Trace min node's ancestors.
            min_node >>= 1
            ancestors.add(min_node)

        first_common_ancestor = 1  # Default to the root which is 1.
        while max_node > 1:  # Trace max node's ancestors.
            max_node >>= 1
            if max_node in ancestors:  # Both nodes' first common ancestor.
                first_common_ancestor = max_node
                break
            ancestors.add(max_node)

        # Exclude "0b" prefix to have real bin len. Real bin len - 1 = level.
        first_common_ancestor_level = len(bin(first_common_ancestor)) - 3
        answers.append(min_node_level + max_node_level + 1)
        answers[-1] -= 2 * first_common_ancestor_level
        ancestors.clear()  # Reset for the next query.

    return answers
