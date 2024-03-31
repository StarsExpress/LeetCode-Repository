
def quick_sort_list(input_array: list | tuple | set, pivot_choice: str = 'median'):
    if len(input_array) <= 1:
        return input_array, 0

    if pivot_choice == 'first':  # In any pivot choice, always ensure pivot ends up at 1st place of list.
        pivot = input_array[0]

    else:
        if pivot_choice == 'last':
            pivot = input_array[-1]

        else:  # Median of the three (1st item, middle item, last item) method.
            medians = [input_array[0], input_array[-1]]
            if len(input_array) % 2 == 1:
                medians.append(input_array[len(input_array) // 2])

            else:
                medians.append(input_array[len(input_array) // 2 - 1])

            medians.sort()
            pivot = medians.pop(1)
            del medians

        pivot_idx = input_array.index(pivot)
        input_array[0], input_array[pivot_idx] = input_array[pivot_idx], input_array[0]
        del pivot_idx

    front_idx, back_idx = 1, 1  # Both front and back indices start at 2nd item to "ensure 2nd item <= pivot".

    while front_idx < len(input_array):  # Until front index reaches the end.
        if input_array[front_idx] < pivot:  # Switch items at front and back indices.
            input_array[back_idx], input_array[front_idx] = input_array[front_idx], input_array[back_idx]
            back_idx += 1  # Whenever a switch happens, increment back index.

        front_idx += 1  # Always increment front index.

    # Switch pivot with item at back index - 1.
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
