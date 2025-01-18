
def harvest_max_fruits(fruits: list[list[int]], start_position: int, steps: int) -> int:  # LeetCode Q.2106.
    positions2fruits = {position: fruit for position, fruit in fruits}

    route_1_min_position = start_position - steps  # Route 1: go right and turn left.
    route_1_max_position = start_position

    route_1_fruits = 0
    for position in range(start_position - steps, start_position + 1):
        if position in positions2fruits.keys():
            route_1_fruits += positions2fruits[position]

    route_2_min_position = start_position  # Route 2: go left and turn right.
    route_2_max_position = start_position + steps

    route_2_fruits = 0
    for position in range(start_position, start_position + steps + 1):
        if position in positions2fruits.keys():
            route_2_fruits += positions2fruits[position]

    max_fruits = max(route_1_fruits, route_2_fruits)

    max_pre_turn_len = (steps + 1) // 2 - 1
    for _ in range(max_pre_turn_len):
        route_1_min_position += 2
        route_1_max_position += 1

        for position in (route_1_min_position - 2, route_1_min_position - 1):
            if position in positions2fruits.keys():
                route_1_fruits -= positions2fruits[position]

        if route_1_max_position in positions2fruits.keys():
            route_1_fruits += positions2fruits[route_1_max_position]

        route_2_min_position -= 1
        route_2_max_position -= 2

        for position in (route_2_max_position + 1, route_2_max_position + 2):
            if position in positions2fruits.keys():
                route_2_fruits -= positions2fruits[position]

        if route_2_min_position in positions2fruits.keys():
            route_2_fruits += positions2fruits[route_2_min_position]

        if max(route_1_fruits, route_2_fruits) > max_fruits:
            max_fruits = max(route_1_fruits, route_2_fruits)

    return max_fruits
