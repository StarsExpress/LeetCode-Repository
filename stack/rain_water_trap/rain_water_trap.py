
def calculate_trapped_water(heights: list[int]) -> int:  # LeetCode Q.42.
    stack: list[tuple[int, int]] = []  # Height decreasing monotonic stack. Format: (height, idx).
    trapped_water = 0
    for idx, height in enumerate(heights):
        anchor_height = 0
        while stack:
            width = (idx - 1 - stack[-1][1])
            trapped_water += (min(height, stack[-1][0]) - anchor_height) * width
            if stack[-1][0] > height:
                break  # Stop when seeing a left taller bar.
            
            anchor_height = stack[-1][0]  # Anchors for next encountered left height.
            stack.pop(-1)  # My right bars can't work with left bars no taller than me.

        stack.append((height, idx))

    return trapped_water
