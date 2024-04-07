
def quick_sort(array: list | tuple, pivot_choice: str = 'median'):
    if len(array) <= 1:
        return array, 0

    if pivot_choice == 'first':  # In any pivot choice, always ensure pivot ends up at 1st place of list.
        pivot = array[0]

    else:
        if pivot_choice == 'last':
            pivot = array[-1]

        else:  # Median of the three (1st item, middle item, last item) method.
            medians = [array[0], array[-1]]
            if len(array) % 2 == 1:
                medians.append(array[len(array) // 2])

            else:
                medians.append(array[len(array) // 2 - 1])

            medians.sort()
            pivot = medians.pop(1)

        pivot_idx = array.index(pivot)
        array[0], array[pivot_idx] = array[pivot_idx], array[0]

    front_idx, back_idx = 1, 1  # Both front and back indices start at 2nd item to "ensure 2nd item <= pivot".

    while front_idx < len(array):  # Until front index reaches the end.
        if array[front_idx] < pivot:  # Switch items at front and back indices.
            array[back_idx], array[front_idx] = array[front_idx], array[back_idx]
            back_idx += 1  # Whenever a switch happens, increment back index.

        front_idx += 1  # Always increment front index.

    # Switch pivot with item at back index - 1.
    array[0], array[back_idx - 1] = array[back_idx - 1], array[0]

    array[:back_idx - 1], back_comparisons_count = quick_sort(array[:back_idx - 1], pivot_choice)
    array[back_idx:], front_comparisons_count = quick_sort(array[back_idx:], pivot_choice)

    return array, back_comparisons_count + front_comparisons_count + len(array) - 1


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    integers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers', 'int_10k.txt')
    lines = open(integers_array_path, 'r').readlines()
    integers_list = [int(line.strip()) for line in lines]
    print(quick_sort(integers_list)[1])
