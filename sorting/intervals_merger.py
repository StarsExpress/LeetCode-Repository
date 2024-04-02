
def merge_sort(list_of_list_1: list[list], list_of_list_2: list[list]):
    merged_list, idx_1, idx_2 = [], 0, 0

    while idx_1 < len(list_of_list_1) and idx_2 < len(list_of_list_2):
        if list_of_list_1[idx_1][0] <= list_of_list_2[idx_2][0]:
            merged_list.append(list_of_list_1[idx_1])
            idx_1 += 1
            continue

        merged_list.append(list_of_list_2[idx_2])
        idx_2 += 1

    merged_list.extend(list_of_list_1[idx_1:] + list_of_list_2[idx_2:])
    return merged_list


def sort_list(list_of_list: list[list]):
    if len(list_of_list) <= 1:
        return list_of_list

    center_idx = len(list_of_list) // 2
    sorted_list_1 = sort_list(list_of_list[:center_idx])
    sorted_list_2 = sort_list(list_of_list[center_idx:])
    return merge_sort(sorted_list_1, sorted_list_2)


def merge_intervals(intervals: list[list[int]]):  # LeetCode Q.56.
    if len(intervals) <= 0:
        raise IndexError('Empty intervals.')
    if len(intervals) == 1:
        return intervals

    intervals, left_idx, right_idx = sort_list(intervals), 0, 1
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
        right_idx += left_idx - right_idx + 1


if __name__ == '__main__':
    print(merge_intervals([[2,3],[4,5],[6,7],[8,9],[1,10]]))
