
def find_min_buses_route(routes: list[list[int]], source: int, target: int) -> int:  # LeetCode Q.815.
    if source == target:  # Base case.
        return 0

    source_routes, target_routes = set(), set()
    routes_intersections: dict[int, set[int]] = dict()

    total_routes = len(routes)
    for route_1, route_1_stops in enumerate(routes):
        if source in route_1_stops:
            source_routes.add(route_1)

        if target in route_1_stops:
            target_routes.add(route_1)

        if route_1 not in routes_intersections.keys():
            routes_intersections.update({route_1: set()})

        for route_2 in range(route_1 + 1, total_routes):
            route_2_stops = routes[route_2]
            if set(route_1_stops) & set(route_2_stops) != set():
                routes_intersections[route_1].add(route_2)
                if route_2 not in routes_intersections.keys():
                    routes_intersections.update({route_2: set()})
                routes_intersections[route_2].add(route_1)

    if target_routes:  # Target stop has bus routes.
        taken_routes = set()
        # Format: (current route, buses taken).
        queue = [(route, 1) for route in source_routes]

        while queue:
            current_route, buses_taken = queue.pop(0)
            if target in routes[current_route]:
                return buses_taken

            if current_route not in taken_routes:
                taken_routes.add(current_route)
                buses_taken += 1
                if current_route in routes_intersections.keys():
                    for intersection_route in routes_intersections[current_route]:
                        if intersection_route not in taken_routes:
                            queue.append((intersection_route, buses_taken))

    return -1
