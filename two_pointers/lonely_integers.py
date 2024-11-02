
def find_lonely_integers(numbers: list[int]) -> list[int]:  # LeetCode Q.2150.
    counts: dict[int, int] = dict()
    occurred_numbers, lonely_nums = set(), []
    for number in numbers:
        if number not in counts.keys():
            occurred_numbers.add(number)
            counts.update({number: 0})
        counts[number] += 1

    for number in occurred_numbers:
        if counts[number] == 1 and {number - 1, number + 1} & occurred_numbers == set():
            lonely_nums.append(number)

    return lonely_nums
