
def count_split_inversions(nums_list_1, nums_list_2):
    merged_list, split_inversions, list_1_idx, list_2_idx = [], 0, 0, 0

    while list_1_idx < len(nums_list_1) and list_2_idx < len(nums_list_2):
        if nums_list_1[list_1_idx] <= nums_list_2[list_2_idx]:
            merged_list.append(nums_list_1[list_1_idx])
            list_1_idx += 1

        else:
            merged_list.append(nums_list_2[list_2_idx])
            split_inversions += len(nums_list_1) - list_1_idx
            list_2_idx += 1

    merged_list.extend(nums_list_1[list_1_idx:] + nums_list_2[list_2_idx:])
    del nums_list_1, nums_list_2
    return merged_list, split_inversions


def merge_sort_list(nums_list):
    if len(nums_list) <= 1:
        return nums_list, 0

    center_index = len(nums_list) // 2
    nums_list_part_1, left_inversions = merge_sort_list(nums_list[:center_index])
    nums_list_part_2, right_inversions = merge_sort_list(nums_list[center_index:])
    merged_list, split_inversions = count_split_inversions(nums_list_part_1, nums_list_part_2)
    return merged_list, left_inversions + right_inversions + split_inversions


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    integers_array_path = os.path.join(DATA_FOLDER_PATH, 'integers_100000.txt')
    lines = open(integers_array_path, 'r').readlines()
    integers_list = [int(line.strip()) for line in lines]
    print(merge_sort_list(integers_list)[1])
