
def quick_sort_list(input_array: list | tuple | set, pivot_choice: str = 'median'):
    if len(input_array) <= 1:
        return input_array, 0

    if pivot_choice == 'first':  # In any pivot choice, always ensure pivot ends up at 1st place of list.
        pivot = input_array[0]

    else:
        if pivot_choice == 'last':
            pivot = input_array[-1]

        else:  # Median of the three (1st item, middle item, last item) method.
            median_of_3_list = [input_array[0], input_array[-1]]
            if len(input_array) % 2 == 1:
                median_of_3_list.append(input_array[len(input_array) // 2])

            else:
                median_of_3_list.append(input_array[len(input_array) // 2 - 1])

            median_of_3_list.sort()
            pivot = median_of_3_list[1]
            del median_of_3_list

        pivot_idx = input_array.index(pivot)
        input_array[0], input_array[pivot_idx] = input_array[pivot_idx], input_array[0]
        del pivot_idx

    front_idx, back_idx = 1, 1  # Both front and back indices start at 2nd item.

    while front_idx < len(input_array):  # Once front index reaches the end, break while.
        if input_array[front_idx] < pivot:  # Switch items at front and back indices.
            input_array[back_idx], input_array[front_idx] = input_array[front_idx], input_array[back_idx]
            back_idx += 1  # Only increment back index when swap happens.

        front_idx += 1  # Always increment front index.

    # Switch pivot with the item at back index - 1.
    input_array[0], input_array[back_idx - 1] = input_array[back_idx - 1], input_array[0]

    input_array[:back_idx - 1], back_comparisons_count = quick_sort_list(input_array[:back_idx - 1], pivot_choice)
    input_array[back_idx:], front_comparisons_count = quick_sort_list(input_array[back_idx:], pivot_choice)

    return input_array, back_comparisons_count + front_comparisons_count + len(input_array) - 1


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    integers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers', 'int_10k.txt')
    lines = open(integers_array_path, 'r').readlines()
    integers_list = [int(line.strip()) for line in lines]
    print(quick_sort_list(integers_list)[1])
