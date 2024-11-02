
def split_triplets(numbers: list[int]) -> list[int]:  # LeetCode Q.927.
    total_sum = sum(numbers)
    if total_sum % 3 != 0:  # Base case.
        return [-1, -1]
    if total_sum == 0:  # Base case.
        return [0, 2]

    total_nums, one_third = len(numbers), total_sum // 3
    encountered_ones, ending_zeros = 0, 0
    first_idx, second_idx, third_idx = None, None, None

    for idx, number in enumerate(numbers):
        if number == 1:
            encountered_ones += 1

        if encountered_ones == one_third and first_idx is None:  # 1st separation.
            first_idx = idx

        if encountered_ones == 2 * one_third and second_idx is None:  # 2nd separation.
            second_idx = idx + 1

        if encountered_ones == 2 * one_third + 1 and third_idx is None:
            third_idx = idx

        if encountered_ones == total_sum:  # Location of the last 1.
            ending_zeros += total_nums - 1 - idx
            break

    if second_idx - 1 + ending_zeros >= third_idx:
        return [-1, -1]
    second_idx += ending_zeros

    first_idx += ending_zeros
    if first_idx >= second_idx:
        return [-1, -1]

    first_number = int("".join(str(num) for num in numbers[:first_idx + 1]), 2)
    second_number = int("".join(str(num) for num in numbers[first_idx + 1: second_idx]), 2)
    if first_number != second_number:
        return [-1, -1]

    third_number = int("".join(str(num) for num in numbers[second_idx:]), 2)
    if second_number != third_number:
        return [-1, -1]
    return [first_idx, second_idx]
