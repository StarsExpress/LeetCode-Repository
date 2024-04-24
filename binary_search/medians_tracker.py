
def binary_search(target: int | float, sorted_numbers: list[int | float] | tuple[int | float]):
    if len(sorted_numbers) <= 0:
        return 0

    back_idx, front_idx = 0, len(sorted_numbers) - 1
    while True:
        if back_idx > front_idx:
            return back_idx  # Number of ints < target.

        mid_idx = (back_idx + front_idx) // 2
        if sorted_numbers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1


def track_medians(numbers: list[int | float] | tuple[int | float], return_sum=False, only_last_4_digits=False):
    if len(numbers) <= 0:
        return 0

    medians, sorted_items, sorted_items_size = [], [], 0  # Track size of sorted items.
    while numbers:
        newcomer = numbers.pop(0)
        insertion_idx = binary_search(newcomer, sorted_items)
        sorted_items.insert(insertion_idx, newcomer)
        sorted_items_size += 1  # Update size.
        if sorted_items_size % 2 == 1:
            medians.append(sorted_items[sorted_items_size // 2])
            continue

        # For even items count, median is defined as the (count / 2)th "smallest".
        medians.append(sorted_items[(sorted_items_size // 2) - 1])

    assert len(numbers) + len(sorted_items) == len(medians)

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
