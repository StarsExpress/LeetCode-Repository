
def count_split_inversions(input_array_1: list | tuple | set, input_array_2: list | tuple | set):
    merged_list, split_inversions, list_1_idx, list_2_idx = [], 0, 0, 0

    while list_1_idx < len(input_array_1) and list_2_idx < len(input_array_2):
        if input_array_1[list_1_idx] <= input_array_2[list_2_idx]:
            merged_list.append(input_array_1[list_1_idx])
            list_1_idx += 1

        else:
            merged_list.append(input_array_2[list_2_idx])
            split_inversions += len(input_array_1) - list_1_idx
            list_2_idx += 1

    merged_list.extend(input_array_1[list_1_idx:] + input_array_2[list_2_idx:])
    del input_array_1, input_array_2
    return merged_list, split_inversions


def merge_sort_list(input_array: list | tuple | set):
    if len(input_array) <= 1:
        return input_array, 0

    center_index = len(input_array) // 2
    nums_list_part_1, left_inversions = merge_sort_list(input_array[:center_index])
    nums_list_part_2, right_inversions = merge_sort_list(input_array[center_index:])
    merged_list, split_inversions = count_split_inversions(nums_list_part_1, nums_list_part_2)
    return merged_list, left_inversions + right_inversions + split_inversions


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    integers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers', 'int_100k.txt')
    lines = open(integers_array_path, 'r').readlines()
    integers_list = [int(line.strip()) for line in lines]
    print(merge_sort_list(integers_list)[1])
