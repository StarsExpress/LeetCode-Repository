
def find_min_price(
    total_cities: int, flights: list[list[int]], source: int, destination: int, stops_limit: int
) -> int:  # LeetCode Q.787.
    adjacency_matrix: list[list[tuple[int, int]]] = [[] for _ in range(total_cities)]
    for start, destination, price in flights:
        adjacency_matrix[start].append((destination, price))

    min_cost = [float("inf")] * total_cities
    queue = [(source, 0, 0)]  # Format: (current city, current cost, used stops).
    while queue:
        current_city, current_cost, used_stops = queue.pop(0)
        for neighbor, price in adjacency_matrix[current_city]:
            new_cost = current_cost + price
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                if used_stops + 1 <= stops_limit:
                    queue.append((neighbor, new_cost, used_stops + 1))

    return -1 if min_cost[destination] == float("inf") else min_cost[destination]
