from trees.min_heap import MinHeap
from trees.max_heap import MaxHeap
from copy import deepcopy


def track_median(items_list, return_sum=False, only_last_4_digits=False):
    if len(items_list) <= 0:
        return None

    items_list = deepcopy(items_list)  # Prevent popping from modifying original list.

    medians_list = []
    min_heap, max_heap = MinHeap([]), MaxHeap([])  # Initialize both heaps with empty lists.
    while True:
        if len(items_list) <= 0:
            break

        current_item = items_list.pop(0)
        if len(medians_list) <= 0:
            min_heap.add_items(current_item)
            medians_list.append(current_item)
            continue

        if current_item < medians_list[-1]:
            max_heap.add_items(current_item)

        else:
            min_heap.add_items(current_item)

        if len(max_heap.items_list) - 1 > len(min_heap.items_list):  # Ensure heaps size diff <= 1.
            max_heap_root = max_heap.find_max(remove=True)
            min_heap.add_items(max_heap_root)

        if len(min_heap.items_list) - 1 > len(max_heap.items_list):  # Ensure heaps size diff <= 1.
            min_heap_root = min_heap.find_min(remove=True)
            max_heap.add_items(min_heap_root)

        # Equal sign takes max heap's root: for even items count, median is defined as the (count / 2)th "smallest".
        if len(min_heap.items_list) <= len(max_heap.items_list):
            medians_list.append(max_heap.find_max(remove=False))
            continue
        medians_list.append(min_heap.find_min(remove=False))

    assert len(min_heap.items_list) + len(max_heap.items_list) == len(medians_list)

    if return_sum:
        medians_sum = sum(medians_list)
        if only_last_4_digits:
            medians_sum %= 10000
        return medians_sum

    return medians_list


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os
    import time

    start_time = time.time()
    numbers_array_path = os.path.join(DATA_FOLDER_PATH, 'num_10k.txt')
    lines = open(numbers_array_path, 'r').readlines()
    numbers_list = [int(line.strip()) for line in lines]
    print(track_median(numbers_list, True))

    end_time = time.time()
    print(f'Total runtime: {str(round(end_time - start_time, 2))} seconds on {len(numbers_list)} items.\n')