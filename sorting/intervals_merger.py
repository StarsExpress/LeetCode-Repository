
def _sort_intervals(list_of_list: list[list[int]]) -> list[list[int]]:
    if len(list_of_list) <= 1:
        return list_of_list

    pivot, front_idx, back_idx = list_of_list[0], 1, 1

    while front_idx < len(list_of_list):  # Until front idx reaches the end.
        if list_of_list[front_idx][0] < pivot[0]:  # Switch items at front and back indices.
            list_of_list[back_idx], list_of_list[front_idx] = list_of_list[front_idx], list_of_list[back_idx]
            back_idx += 1  # Whenever a switch happens, increment back idx.

        front_idx += 1  # Always increment front idx.

    # Switch pivot with item at back idx - 1.
    list_of_list[0], list_of_list[back_idx - 1] = list_of_list[back_idx - 1], list_of_list[0]

    list_of_list[:back_idx - 1] = _sort_intervals(list_of_list[:back_idx - 1])
    list_of_list[back_idx:] = _sort_intervals(list_of_list[back_idx:])
    return list_of_list


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:  # LeetCode Q.56.
    if len(intervals) == 1:
        return intervals

    intervals, left_idx, right_idx = _sort_intervals(intervals), 0, 1
    while True:
        if right_idx >= len(intervals):
            return intervals

        if intervals[left_idx][1] < intervals[right_idx][0]:
            left_idx += 1
            right_idx += 1
            continue

        merged = [min(intervals[left_idx][0], intervals[right_idx][0]),
                  max(intervals[left_idx][1], intervals[right_idx][1])]
        intervals.pop(right_idx)
        intervals.pop(left_idx)
        intervals.insert(left_idx, merged)
        right_idx += left_idx + 1 - right_idx
