
class RedundantDirectedEdge:  # LeetCode Q.685.
    def __init__(self):
        self.graph: dict[int, set[int]] = dict()
        self.visited_nodes: set[int] = set()

    def _test_connection(self, start_node: int, end_node: int) -> bool:
        self.visited_nodes.clear()
        if start_node in self.graph.keys() and end_node in self.graph[start_node]:
            self.graph[start_node].remove(end_node)
            connection = self._dfs_connection(start_node, end_node)
            self.graph[start_node].add(end_node)  # Restore the edge.

        else:
            connection = self._dfs_connection(start_node, end_node)

        return connection

    def _dfs_connection(self, start_node: int, end_node: int) -> bool:
        self.visited_nodes.add(start_node)
        if start_node in self.graph.keys():
            for neighbor_node in self.graph[start_node]:
                if neighbor_node == end_node:
                    return True

                if neighbor_node not in self.visited_nodes:
                    if self._dfs_connection(neighbor_node, end_node):
                        return True

        return False

    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        self.graph.clear()  # Reset before search.

        in_degrees: dict[int, int] = dict()  # Each node's in degree.

        visited_edges: set[str] = set()  # Format: str(out edge) + ":" + str(in edge).
        opposite_edges: list[list[int]] = []  # Two opposite edges: answer must be one of them.

        for out_node, in_node in edges:
            if out_node not in self.graph.keys():
                self.graph.update({out_node: set()})
            self.graph[out_node].add(in_node)

            for node in (out_node, in_node):
                if node not in in_degrees.keys():
                    in_degrees.update({node: 0})
            in_degrees[in_node] += 1

            if f"{in_node}:{out_node}" in visited_edges:
                opposite_edges.extend(
                    [[in_node, out_node], [out_node, in_node]]
                )
            visited_edges.add(f"{out_node}:{in_node}")

        root = None
        for node, in_degree in in_degrees.items():  # Detect root.
            if in_degree == 0:  # No incoming edges: root.
                root = node
                break

        # Reverse traversal: when multiple answers occur, always pick the last.
        for out_node, in_node in opposite_edges[::-1]:
            if root is None:  # An edge goes into root, preventing detection.
                if in_degrees[in_node] == 1:  # Remove current edge: root shows up.
                    return [out_node, in_node]
                return opposite_edges[0]  # Must remove the other edge.

            # Root is detected: all other nodes' in-degrees = 1 after edge removal.
            if in_degrees[in_node] == 1:  # Remove current edge: gets another root.
                return opposite_edges[0]  # Must remove the other edge.
            return [out_node, in_node]

        # Reverse traversal: when multiple answers occur, always pick the last.
        for out_node, in_node in edges[::-1]:
            if root is None:  # Root not detected yet.
                if in_degrees[in_node] == 1:
                    if self._test_connection(in_node, out_node):
                        return [out_node, in_node]

            else:  # Root is detected.
                if in_degrees[in_node] == 2:
                    # Pulling off this edge won't cause graph disconnection.
                    if root != out_node or self._test_connection(root, in_node):
                        return [out_node, in_node]

        return []
