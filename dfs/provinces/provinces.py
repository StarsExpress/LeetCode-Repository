
class Provinces:  # LeetCode Q.547.
    def count_provinces(self, connections: list[list[int]]) -> int:
        self.graph: list[list[int]] = connections
        self.visited_cities: set[int] = set()
        total_capitals = 0

        for city_1 in range(len(self.graph)):
            if city_1 not in self.visited_cities:
                total_capitals +=1
                self._dfs_provinces(city_1)

        return total_capitals

    def _dfs_provinces(self, city: int) -> None:
        self.visited_cities.add(city)
        for next_city in range(len(self.graph[city])):
            if self.graph[city][next_city] == 1:
                if next_city not in self.visited_cities:
                    self._dfs_provinces(next_city)
