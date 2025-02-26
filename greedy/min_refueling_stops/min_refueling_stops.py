import heapq


def compute_min_stops(target: int, start_fuel: int, stations: list[list[int]]) -> int:  # LeetCode Q.871.
    stops, fuel_max_heap = 0, []
    current_position, current_fuel = start_fuel, 0
    while current_position < target:
        while stations and current_position >= stations[0][0]:  # Visitable stations.
            heapq.heappush(fuel_max_heap, -stations.pop(0)[1])  # Negate for max heap.

        while current_fuel <= 0:
            if not fuel_max_heap:  # Past gas stations are all visited.
                return -1
            current_fuel -= heapq.heappop(fuel_max_heap)
            stops += 1

        current_position += current_fuel
        current_fuel -= current_fuel  # All fuel is used to forward position.

    return stops
