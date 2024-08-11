
def find_longest_subarray(integers: list[int], limit: int):  # LeetCode Q.1438.
    total_len = len(integers)
    if total_len <= 1:
        return total_len

    current_idx, subarray, max_len = 1, [integers[0]], 1
    last_min, last_max = integers[0], integers[0]
    while True:
        if current_idx >= len(integers):
            return max(max_len, len(subarray))

        newcomer = integers[current_idx]
        subarray.append(newcomer)
        if newcomer < last_min:  # Update min and max if needed.
            last_min = newcomer
        if newcomer > last_max:
            last_max = newcomer

        if last_max - last_min > limit:  # If newcomer causes limit explosion.
            if len(subarray) - 1 > max_len:  # -1 excludes newcomer when updating max len.
                max_len = len(subarray) - 1

            while subarray:
                if max(subarray) - min(subarray) > limit:
                    subarray.pop(0)
                break

            last_min, last_max = min(subarray), max(subarray)

        current_idx += 1
