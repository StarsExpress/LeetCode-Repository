
def count_visibilities(heights: list[int]) -> list[int]:  # LeetCode Q.1944.
    stack = []  # Height decreasing monotonic stack.
    visibilities = []
    for height in heights[::-1]:  # Backward iteration.
        visibilities.append(0)  # My (if I am the rightmost) min visibility is 0.

        while stack and stack[-1] <= height:  # People on my left side can't see them.
            stack.pop(-1)
            visibilities[-1] += 1

        if stack:  # I can always see my next taller person (if exists).
            visibilities[-1] += 1

        stack.append(height)

    return visibilities[::-1]  # Revert back to original order.
