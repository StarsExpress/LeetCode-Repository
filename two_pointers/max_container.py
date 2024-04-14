
def seek_max_volume(heights: list[int]):  # LeetCode Q.11.
    back_idx, front_idx, current_volume, max_volume = 0, len(heights) - 1, 0, 0

    while True:
        if back_idx >= front_idx:
            return max_volume

        current_volume += min(heights[back_idx], heights[front_idx]) * (front_idx - back_idx) - current_volume
        if current_volume > max_volume:
            max_volume += current_volume - max_volume

        if heights[back_idx] <= heights[front_idx]:
            back_idx += 1
            continue
        front_idx -= 1
