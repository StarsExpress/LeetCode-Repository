
class RedundantUndirectedEdge:  # LeetCode Q.684.
    def __init__(self):
        self.parents: dict[int, int] = dict()

    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        self.parents.clear()  # Reset before search.
        distinct_nodes = set(sum(edges, []))
        for node in distinct_nodes:
            self.parents.update({node: node})

        redundant_connection = []
        for node_1, node_2 in edges:
            parent_1 = self._find_parent(node_1)
            parent_2 = self._find_parent(node_2)
            if parent_1 == parent_2:  # Current edge is redundant.
                redundant_connection.extend([node_1, node_2])
                break
            self._union_nodes(node_1, node_2)

        return redundant_connection

    def _find_parent(self, node: int) -> int:
        parent = self.parents[node]
        return node if parent == node else self._find_parent(parent)

    def _union_nodes(self, node_1: int, node_2: int) -> None:
        parent_1 = self._find_parent(node_1)
        parent_2 = self._find_parent(node_2)
        if parent_1 != parent_2:
            self.parents[parent_2] = parent_1
