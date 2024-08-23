
def _count_smaller(target: int, sorted_integers: list[int] | tuple[int]):
    """Count number of integers smaller than target."""
    if not sorted_integers:
        return 0

    back_idx, front_idx = 0, len(sorted_integers) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target.


def compute_sorting_cost(numbers: list[int] | tuple[int]):  # LeetCode Q.1649.
    sorted_nums, hash_table = [], dict()
    total_cost = 0
    for number in numbers:  # Don't use pop due to slower speed.
        if number not in hash_table.keys():
            hash_table.update({number: 0})

        smaller_count = _count_smaller(number, sorted_nums)
        # Smaller or equal count: smaller count + past occurrence.
        bigger_count = len(sorted_nums) - (smaller_count + hash_table[number])
        total_cost += min(smaller_count, bigger_count)

        sorted_nums.insert(smaller_count, number)  # Smaller count = insertion idx.
        hash_table[number] += 1
    
    return total_cost % (10 ** 9 + 7)
