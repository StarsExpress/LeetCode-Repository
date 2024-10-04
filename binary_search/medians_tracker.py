
def _binary_search(target: int | float, sorted_numbers: list[int | float], size: int) -> int:
    if size == 0:
        return 0

    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_numbers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target.


def track_medians(
    numbers: list[int | float], return_sum=False, only_last_4_digits=False
) -> int | list[int | float]:
    if not numbers:
        return 0

    medians, sorted_numbers, count = [], [], 0  # Track count of sorted numbers.
    while numbers:
        newcomer = numbers.pop(0)
        insertion_idx = _binary_search(newcomer, sorted_numbers, count)
        sorted_numbers.insert(insertion_idx, newcomer)
        count += 1  # Update size.
        if count % 2 == 1:
            medians.append(sorted_numbers[count // 2])
            continue

        # For even count, median is defined as the (count / 2)th "smallest".
        medians.append(sorted_numbers[(count // 2) - 1])

    if return_sum:
        medians_sum = sum(medians)
        if only_last_4_digits:
            medians_sum %= 10000
        return medians_sum
    return medians
