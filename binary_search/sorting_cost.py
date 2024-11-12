
def _count_smaller(target: int, sorted_integers: list[int], size: int) -> int:
    """Count number of integers smaller than target."""
    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target.


def compute_sorting_cost(numbers: list[int]) -> int:  # LeetCode Q.1649.
    occurrences_table = dict()
    sorted_nums, total_nums = [], 0
    total_cost = 0
    for number in numbers:
        if number not in occurrences_table.keys():
            occurrences_table.update({number: 0})

        smaller_count = _count_smaller(number, sorted_nums, total_nums)
        bigger_count = total_nums - smaller_count - occurrences_table[number]
        total_cost += min(smaller_count, bigger_count)

        sorted_nums.insert(smaller_count, number)
        total_nums += 1
        occurrences_table[number] += 1

    return total_cost % (10 ** 9 + 7)
