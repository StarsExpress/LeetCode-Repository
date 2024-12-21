
def compute_collision_times(cars: list[list[int]]) -> list[float]:  # LeetCode Q.1776.
    collision_times = []
    # Speed increasing monotonic stack. Format: (position, speed).
    stack: list[tuple[int, int]] = []

    for position, speed in cars[::-1]:  # From rightmost to leftmost.
        # The stack[-1] car can't be crashed by its left side cars.
        while stack and stack[-1][1] >= speed:
            stack.pop(-1)

        # Cars at stack[-1] and stack[-2] crash.
        while len(stack) >= 2 and stack[-1][1] > stack[-2][1]:
            # Crash time of current and stack[-1] cars.
            crash_time_1 = (stack[-1][0] - position) / (speed - stack[-1][1])

            # Crash time of stack[-1] and stack[-2] cars.
            crash_time_2 = (stack[-2][0] - stack[-1][0]) / (stack[-1][1] - stack[-2][1])

            if crash_time_1 <= crash_time_2:  # Current car crashes stack[-1] car.
                break

            stack.pop(-1)  # The stack[-1] car is already united into stack[-2] car.

        if stack and speed > stack[-1][1]:  # Current car crashes stack[-1] car.
            collision_times.append(
                (stack[-1][0] - position) / (speed - stack[-1][1])
            )

        else:  # Current car never crashes any car.
            collision_times.append(-1)

        stack.append((position, speed))

    return collision_times[::-1]  # Revert back to the original order.
