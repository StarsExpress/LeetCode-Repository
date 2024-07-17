
class DivisionEvaluator:  # LeetCode Q.399.
    def __init__(self):
        self.graph = dict()

    def evaluate(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ):
        self.graph.clear()  # Reset before evaluation.

        while equations:
            numerator, denominator = equations.pop(0)
            value = values.pop(0)

            if numerator not in self.graph.keys():
                self.graph.update({numerator: dict()})
            self.graph[numerator].update({denominator: value})

            if denominator not in self.graph.keys():
                self.graph.update({denominator: dict()})
            self.graph[denominator].update({numerator: 1 / value})

        graph_nodes = set(self.graph.keys())
        division_results = []
        while queries:
            numerator, denominator = queries.pop(0)

            if numerator not in graph_nodes or denominator not in graph_nodes:
                division_results.append(-1)
                continue

            if numerator == denominator:
                division_results.append(1)
                continue

            final_division = self._dfs_graph(numerator, denominator, 1, set())
            if final_division:
                division_results.append(final_division)
                continue

            division_results.append(-1)

        return division_results

    def _dfs_graph(
        self,
        start: str,
        destination: str,
        rolling_division: int,
        visited_stops: set[str],
    ):
        visited_stops.add(start)
        if destination in self.graph[start].keys():
            return rolling_division * self.graph[start][destination]

        mid_stops = set(self.graph[start].keys())
        mid_stops -= mid_stops.intersection(visited_stops)
        if len(mid_stops) == 0:
            return None

        for mid_stop in mid_stops:
            final_division = self._dfs_graph(
                mid_stop,
                destination,
                rolling_division * self.graph[start][mid_stop],
                visited_stops
            )

            if final_division is not None:
                return final_division

        return None  # DFS end. No (start, destination) pair found.
