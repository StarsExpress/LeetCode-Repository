
def compute_sorting_cost(numbers: list[int]) -> int:  # LeetCode Q.1649.
    occurrences_table = dict()
    sorted_numbers, total_numbers = [], 0
    total_cost = 0
    for number in numbers:
        if number not in occurrences_table.keys():
            occurrences_table.update({number: 0})

        left_idx, right_idx = 0, total_numbers - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if sorted_numbers[mid_idx] < number:
                left_idx = mid_idx + 1
                continue
            right_idx = mid_idx - 1

        # Back idx: number of ints < target.
        bigger_count = total_numbers - left_idx - occurrences_table[number]
        total_cost += min(left_idx, bigger_count)

        sorted_numbers.insert(left_idx, number)  # Back idx implies insertion idx.
        total_numbers += 1
        occurrences_table[number] += 1

    return total_cost % (10 ** 9 + 7)
