from heaps.min_heap import MinHeap
from heaps.max_heap import MaxHeap


def track_medians(numbers: list[int | float], return_sum=False, only_last_4_digits=False):
    if not numbers:
        return 0

    medians, min_heap, max_heap = [], MinHeap([]), MaxHeap([])  # Initialize both heaps with empty lists.
    for number in numbers:
        if not medians:
            min_heap.add_items(number)
            medians.append(number)
            continue

        if number < medians[-1]:
            max_heap.add_items(number)

        else:
            min_heap.add_items(number)

        if len(max_heap.items_list) - 1 > len(min_heap.items_list):  # Ensure heaps size diff <= 1.
            max_heap_root = max_heap.find_max(remove=True)
            min_heap.add_items(max_heap_root)

        if len(min_heap.items_list) - 1 > len(max_heap.items_list):  # Ensure heaps size diff <= 1.
            min_heap_root = min_heap.find_min(remove=True)
            max_heap.add_items(min_heap_root)

        # Equal sign takes max heap's root: for even items count, median is defined as the (count / 2)th "smallest".
        if len(min_heap.items_list) <= len(max_heap.items_list):
            medians.append(max_heap.find_max(remove=False))
            continue
        medians.append(min_heap.find_min(remove=False))

    assert len(min_heap.items_list) + len(max_heap.items_list) == len(medians)

    if return_sum:
        medians_sum = sum(medians)
        if only_last_4_digits:
            medians_sum %= 10000
        return medians_sum
    return medians


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os
    import time

    start_time = time.time()
    numbers_array_path = os.path.join(DATA_FOLDER_PATH, 'numbers', 'num_10k.txt')
    lines = open(numbers_array_path, 'r').readlines()
    numbers_list = [int(line.strip()) for line in lines]
    print(track_medians(numbers_list, True))

    end_time = time.time()
    print(f'Total runtime: {round(end_time - start_time, 2)} seconds on {len(numbers_list)} items.')
