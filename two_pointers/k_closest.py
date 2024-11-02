
def find_k_closest(array: list[int], k: int, target: int) -> list[int]:  # LeetCode Q.658.
    arr_len = len(array)
    back_idx, front_idx = 0, arr_len - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if array[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    if back_idx == arr_len:
        left_idx, right_idx = back_idx - 1, back_idx - 1

    elif back_idx == 0:
        left_idx, right_idx = back_idx, back_idx

    else:
        # Required to take left side when two sides equal.
        if target - array[back_idx - 1] <= array[back_idx] - target:
            left_idx, right_idx = back_idx - 1, back_idx - 1

        else:
            left_idx, right_idx = back_idx, back_idx

    while right_idx + 1 - left_idx < k:
        if left_idx > 0 and right_idx < arr_len - 1:  # Both sides can extend.
            # Required to take left side when two sides equal.
            if target - array[left_idx - 1] <= array[right_idx + 1] - target:
                left_idx -= 1
                continue

            right_idx += 1
            continue

        if left_idx > 0:  # Only left side can extend.
            left_idx -= 1
            continue

        right_idx += 1  # Only right side can extend.

    return array[left_idx: right_idx + 1]
