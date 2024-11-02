
def calculate_trapped_water(heights: list[int]) -> int:  # LeetCode Q.42.
    # Height decreasing monotonic stack.
    stack: list[tuple[int, int]] = []  # Format: (height, idx).
    trapped_water = 0

    for idx, height in enumerate(heights):
        anchor_height = 0

        # My right side heights can't work with left side heights shorter than me.
        while stack and stack[-1][0] < height:
            partner_height, partner_idx = stack.pop(-1)
            trapped_water += (idx - 1 - partner_idx) * (partner_height - anchor_height)
            anchor_height = partner_height  # Anchors for a taller left height.

        if stack:  # I can always work with my previous non-shorter height (if exists).
            partner_idx = stack[-1][1]
            trapped_water += (idx - 1 - partner_idx) * (height - anchor_height)

            # My right side heights can't work with left side height as tall as me.
            if stack[-1][0] == height:
                stack.pop(-1)

        stack.append((height, idx))

    return trapped_water
