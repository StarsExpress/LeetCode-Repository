
def _binary_search(target: int | float, sorted_numbers: list[int | float]):
    if not sorted_numbers:
        return 0

    back_idx, front_idx = 0, len(sorted_numbers) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_numbers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target.


def track_medians(
    numbers: list[int | float],
    return_sum=False,
    only_last_4_digits=False
):
    if not numbers:
        return 0

    medians, sorted_items, sorted_items_size = [], [], 0  # Track size of sorted items.
    while numbers:
        newcomer = numbers.pop(0)
        insertion_idx = _binary_search(newcomer, sorted_items)
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
