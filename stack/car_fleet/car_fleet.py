
def compute_collision_times(cars: list[list[int]]) -> list[float]:  # LeetCode Q.1776.
    total_cars = len(cars)
    collision_times = [-1] * total_cars
    # Speed increasing monotonic stack. Format: (position, speed).
    stack: list[tuple[int, int]] = []

    for reverse_idx, (position, speed) in enumerate(cars[::-1]):
        while stack and stack[-1][1] >= speed:  # Remove all the faster right cars.
            stack.pop(-1)

        while len(stack) >= 2:
            current_car_crash_time = (stack[-2][0] - position) / (speed - stack[-2][1])

            front_car_crash_time = (stack[-2][0] - stack[-1][0]) / (stack[-1][1] - stack[-2][1])

            if current_car_crash_time > front_car_crash_time:
                # Current car and its left cars can't crash stack's last car.
                stack.pop(-1)

            else:  # Current car and its left cars might crash stack's last car.
                break

        idx = total_cars - 1 - reverse_idx
        if stack and speed > stack[-1][1]:
            current_car_crash_time = (stack[-1][0] - position) / (speed - stack[-1][1])
            collision_times[idx] = current_car_crash_time

        stack.append((position, speed))

    return collision_times
