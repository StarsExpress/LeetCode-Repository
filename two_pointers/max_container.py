
def seek_max_volume(heights: list[int]) -> int:  # LeetCode Q.11.
    back_idx, front_idx = 0, len(heights) - 1
    current_volume, max_volume = 0, 0

    while back_idx < front_idx:
        current_volume += min(heights[back_idx], heights[front_idx]) * (front_idx - back_idx) - current_volume
        if current_volume > max_volume:
            max_volume = current_volume

        if heights[back_idx] <= heights[front_idx]:  # Change to another back height.
            back_idx += 1
            continue

        front_idx -= 1  # Change to another front height.

    return max_volume
