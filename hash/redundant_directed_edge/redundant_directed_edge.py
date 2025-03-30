
class RedundantDirectedEdge:  # LeetCode Q.685.
    def __init__(self):
        self.graph: dict[int, set[int]] = dict()
        self.visited_nodes: set[int] = set()

    def _remove_edge(self, out_node: int, in_node: int) -> None:
        if out_node in self.graph.keys() and in_node in self.graph[out_node]:
            self.graph[out_node].remove(in_node)

    def _restore_edge(self, out_node: int, in_node: int) -> None:
        self.graph[out_node].add(in_node)

    def _test_connection(self, start_node: int, target_node: int) -> bool:
        self.visited_nodes.clear()
        return self._dfs_connection(start_node, target_node)

    def _dfs_connection(self, start_node: int, target_node: int) -> bool:
        self.visited_nodes.add(start_node)
        if start_node in self.graph.keys():
            for neighbor_node in self.graph[start_node]:
                if neighbor_node == target_node:
                    return True

                if neighbor_node not in self.visited_nodes:
                    if self._dfs_connection(neighbor_node, target_node):
                        return True

        return False

    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        self.graph.clear()  # Reset before search.

        in_degrees: dict[int, int] = dict()  # Each node's in-degree.
        for out_node, in_node in edges:
            if out_node not in self.graph.keys():
                self.graph.update({out_node: set()})
            self.graph[out_node].add(in_node)

            for node in (out_node, in_node):
                if node not in in_degrees.keys():
                    in_degrees.update({node: 0})
            in_degrees[in_node] += 1

        root = None
        for node, in_degree in in_degrees.items():  # Detect root.
            if in_degree == 0:  # No incoming edges: root.
                root = node
                break

        # Reverse traversal: when multiple answers occur, always pick the last.
        for out_node, in_node in edges[::-1]:
            if root is None:  # Root not detected yet: all nodes have 1 in-degree.
                self._remove_edge(out_node, in_node)
                # W/O this edge, in node can still visit out node.
                if self._test_connection(in_node, out_node):
                    return [out_node, in_node]
                self._restore_edge(out_node, in_node)

            else:  # Root is detected: only one node has 2 in-degree.
                if in_degrees[in_node] == 2:
                    self._remove_edge(out_node, in_node)
                    # W/O this edge, root can still visit in node.
                    if self._test_connection(root, in_node):
                        return [out_node, in_node]
                    self._restore_edge(out_node, in_node)

        return []
