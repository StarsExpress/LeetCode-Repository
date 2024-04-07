
def merge_arrays(array_1: list | tuple, array_2: list | tuple):
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


def merge_sort(array: list | tuple, array_only=False, inversions_only=False):
    if len(array) <= 1:
        return array, 0

    center_idx = len(array) // 2
    array_1, left_inversions = merge_sort(array[:center_idx])
    array_2, right_inversions = merge_sort(array[center_idx:])

    if array_only:
        return merge_arrays(array_1, array_2)[0]
    if inversions_only:
        return left_inversions + right_inversions + merge_arrays(array_1, array_2)[1]

    merged_array, merged_inversions = merge_arrays(array_1, array_2)
    return merged_array, left_inversions + right_inversions + merged_inversions


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    integers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers', 'int_100k.txt')
    lines = open(integers_array_path, 'r').readlines()
    integers_list = [int(line.strip()) for line in lines]
    print(merge_sort(integers_list, inversions_only=True))
