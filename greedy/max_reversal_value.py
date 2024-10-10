
def find_max_reversal_value(numbers: list[int]) -> int:  # LeetCode Q.1330.
    total_numbers, total_value = len(numbers), 0
    # Max of the smaller and min of the bigger of all neighboring numbers.
    max_min, min_max = -float("inf"), float("inf")  # Reversal gain = 2 * max min - min max.

    back_inversion_gain = 0  # Gain by reversing nums[:i] where i != total nums - 1.
    front_inversion_gain = 0  # Gain by reversing nums[i:] where i != 0.

    for i in range(1, total_numbers):
        total_value += abs(numbers[i] - numbers[i - 1])

        if min(numbers[i - 1], numbers[i]) > max_min:
            max_min = min(numbers[i - 1], numbers[i])

        if max(numbers[i - 1], numbers[i]) < min_max:
            min_max = max(numbers[i - 1], numbers[i])

        inversion_gain = abs(numbers[-1] - numbers[i - 1]) - abs(numbers[i] - numbers[i - 1])
        if inversion_gain > front_inversion_gain:
            front_inversion_gain = inversion_gain

        if i < total_numbers - 1:
            inversion_gain = abs(numbers[0] - numbers[i + 1]) - abs(numbers[i] - numbers[i + 1])
            if inversion_gain > back_inversion_gain:
                back_inversion_gain = inversion_gain

    total_value += max(
        2 * (max_min - min_max), back_inversion_gain, front_inversion_gain
    )
    return total_value
