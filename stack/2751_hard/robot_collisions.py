
def find_survivors(positions: list[int], healths: list[int], directions: str) -> list[int]:  # LeetCode Q.2751.
    robots = [
        [idx, position, health, direction]
        for idx, (position, health, direction)
        in enumerate(zip(positions, healths, directions))
    ]
    robots.sort(key=lambda x: x[1])

    stack: list[list[int]] = []  # Format: [idx, health, direction].

    for idx, _, health, direction in robots:
        if direction == "L":  # Current robot might collide with past robots.
            while stack and stack[-1][2] == "R" and health > stack[-1][1]:
                stack.pop(-1)
                health -= 1

            if stack and stack[-1][2] == "R":
                if health == stack[-1][1]:  # Both current and last robot are removed.
                    stack.pop(-1)
                    continue

                stack[-1][1] -= 1  # Last robot's health decrement by 1.
                continue

        stack.append([idx, health, direction])

    stack.sort(key=lambda x: x[0])  # Contains all the remaining robots.
    return [health for _, health, _ in stack]  # Return healths in original idx order.
