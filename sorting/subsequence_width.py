
def count_subsequence_widths(numbers: list[int]) -> int:  # LeetCode Q.891.
    total_width = 0
    maximum_weight, minimum_weight = 1, 2 ** (len(numbers) - 1)
    numbers.sort()
    for number in numbers:
        total_width += (maximum_weight - minimum_weight) * number
        maximum_weight *= 2
        minimum_weight //= 2

    return total_width % (10 ** 9 + 7)  # Required to control size.
