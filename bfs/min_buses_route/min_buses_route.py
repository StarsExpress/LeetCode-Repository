
def find_min_buses_route(routes: list[list[int]], source: int, target: int) -> int:  # LeetCode Q.815.
    if source == target:  # Base case.
        return 0

    # Routes passing through source and target, respectively.
    source_routes, target_routes = set(), set()
    stations2routes: dict[int, list[int]] = dict()

    for route, stations in enumerate(routes):
        route += 1  # Route num = idx + 1.
        for station in stations:
            if station == source:
                source_routes.add(route)

            if station == target:
                target_routes.add(route)

            if station not in stations2routes.keys():
                stations2routes.update({station: []})
            stations2routes[station].append(route)

    if source_routes and target_routes:  # Source to target is possible.
        taken_routes, visited_stations = set(), set()
        # Format: (current route, buses taken).
        queue = [(route, 1) for route in source_routes]

        while queue:
            route, buses_taken = queue.pop(0)
            taken_routes.add(route)
            if route in target_routes:
                return buses_taken

            buses_taken += 1
            for station in routes[route - 1]:  # Route num = idx + 1.
                if station not in visited_stations:
                    visited_stations.add(station)
                    for crossed_route in stations2routes[station]:
                        if crossed_route not in taken_routes:
                            queue.append((crossed_route, buses_taken))

    return -1
