
def merge_sort(array_1: list | tuple | set, array_2: list | tuple | set):
    merged_list, inversions, array_1_idx, array_2_idx = [], 0, 0, 0

    while array_1_idx < len(array_1) and array_2_idx < len(array_2):
        if array_1[array_1_idx] <= array_2[array_2_idx]:
            merged_list.append(array_1[array_1_idx])
            array_1_idx += 1
            continue

        merged_list.append(array_2[array_2_idx])
        inversions += len(array_1) - array_1_idx
        array_2_idx += 1

    merged_list.extend(array_1[array_1_idx:] + array_2[array_2_idx:])
    return merged_list, inversions


def sort_list(input_array: list | tuple | set):
    if len(input_array) <= 1:
        return input_array, 0

    center_idx = len(input_array) // 2
    sorted_list_1, left_inversions = sort_list(input_array[:center_idx])
    sorted_list_2, right_inversions = sort_list(input_array[center_idx:])
    merged_list, merged_inversions = merge_sort(sorted_list_1, sorted_list_2)
    return merged_list, left_inversions + right_inversions + merged_inversions


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    integers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers', 'int_100k.txt')
    lines = open(integers_array_path, 'r').readlines()
    integers_list = [int(line.strip()) for line in lines]
    print(sort_list(integers_list)[1])
