
def compute_heroes_power(numbers: list[int]) -> int:  # LeetCode Q.2681.
    """
    Key: after sorting, for jth number,
    weighted maximums = 1 * (numbers[j + 1] ** 2) + ...... + 2 ** (i - 2) * (numbers[i] ** 2).

    (j + 1)th number's weighted maximums = (jth number's weighted maximums - (j + 1)th number) // 2.
    """
    total_nums = len(numbers)
    if len(set(numbers)) == 1:  # All duplicates. Required to control size.
        return (2 ** total_nums - 1) * (numbers[0] ** 3) % (10 ** 9 + 7)

    numbers.sort()
    weighted_maximums, weight = 0, 1
    for number in numbers[1:]:  # Docstring's formula doesn't contain 0th number.
        weighted_maximums += weight * number ** 2
        weight *= 2

    heroes_power = 0
    for idx, number in enumerate(numbers):
        heroes_power += weighted_maximums * number
        heroes_power += number ** 3  # The subsequence of number itself.

        if idx < total_nums - 1:  # Not last number: adjust weighted maximums.
            weighted_maximums -= numbers[idx + 1] ** 2
            weighted_maximums //= 2

    return heroes_power % (10 ** 9 + 7)  # Required to control size.
