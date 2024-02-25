
def quick_sort_list(nums_list):
    if len(nums_list) <= 1:
        return nums_list, 0

    pivot_choice = 'median'

    if pivot_choice == 'first':  # In any pivot choice, always ensure pivot ends up at 1st place of list.
        pivot = nums_list[0]

    else:
        if pivot_choice == 'last':
            pivot = nums_list[-1]

        else:  # Median of the three (1st item, middle item, last item) method.
            median_of_3_list = [nums_list[0], nums_list[-1]]
            if len(nums_list) % 2 == 1:
                median_of_3_list.append(nums_list[len(nums_list) // 2])

            else:
                median_of_3_list.append(nums_list[len(nums_list) // 2 - 1])

            median_of_3_list.sort()
            pivot = median_of_3_list[1]
            del median_of_3_list

        pivot_idx = nums_list.index(pivot)
        nums_list[0], nums_list[pivot_idx] = nums_list[pivot_idx], nums_list[0]
        del pivot_idx

    front_idx, back_idx = 1, 1  # Both front and back indices start at 2nd item.

    while front_idx < len(nums_list):  # Once front index reaches the end, break while.
        if nums_list[front_idx] < pivot:  # Switch items at front and back indices.
            nums_list[back_idx], nums_list[front_idx] = nums_list[front_idx], nums_list[back_idx]
            back_idx += 1  # Only increment back index when swap happens.

        front_idx += 1  # Always increment front index.

    # Switch pivot with the item at back index - 1.
    nums_list[0], nums_list[back_idx - 1] = nums_list[back_idx - 1], nums_list[0]

    nums_list[:back_idx - 1], back_comparisons_count = quick_sort_list(nums_list[:back_idx - 1])
    nums_list[back_idx:], front_comparisons_count = quick_sort_list(nums_list[back_idx:])

    return nums_list, back_comparisons_count + front_comparisons_count + len(nums_list) - 1


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    integers_array_path = os.path.join(DATA_FOLDER_PATH, 'int_10k.txt')
    lines = open(integers_array_path, 'r').readlines()
    integers_list = [int(line.strip()) for line in lines]
    print(quick_sort_list(integers_list)[1])
