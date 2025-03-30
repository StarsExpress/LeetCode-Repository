
def count_max_robots(charge_times: list[int], running_costs: list[int], budget: int):  # LeetCode Q.2398.
    queue: list[tuple[int, int]] = []  # Format: (charge cost, robot idx).
    running_costs_sum = 0

    # Left & right indices: start & end indices of consecutive robots.
    left_idx, max_robots = 0, 0
    for right_idx in range(len(charge_times)):
        while queue and queue[0][1] < left_idx:
            queue.pop(0)  # Ensure max cost is within selected range.

        while queue and queue[-1][0] <= charge_times[right_idx]:
            queue.pop(-1)  # Prefer bigger charge costs inside queue.

        queue.append((charge_times[right_idx], right_idx))

        running_costs_sum += running_costs[right_idx]
        total_robots = right_idx + 1 - left_idx
        total_cost = queue[0][0] + total_robots * running_costs_sum
        while total_cost > budget:
            running_costs_sum -= running_costs[left_idx]
            left_idx += 1
            total_robots -= 1
            if left_idx > right_idx:  # Can't select the robot at right idx.
                break

            while queue and queue[0][1] < left_idx:
                queue.pop(0)  # Ensure max cost is within selected range.

            total_cost = queue[0][0] + total_robots * running_costs_sum

        if total_robots > max_robots:
            max_robots = total_robots

    return max_robots
