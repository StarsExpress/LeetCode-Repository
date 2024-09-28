
def calculate_max_sum(numbers: list[int]) -> int:  # LeetCode Q.2342.
    digits_sums, max_pair_sum = dict(), -1
    for number in numbers:
        digits_sum = sum(int(digit) for digit in str(number))
        if digits_sum not in digits_sums.keys():
            digits_sums.update({digits_sum: [number]})  # Digit sum and respective max pair.
            continue

        if len(digits_sums[digits_sum]) == 2:
            if number <= digits_sums[digits_sum][0]:  # No need to change anything.
                continue
            digits_sums[digits_sum].pop(0)

        if number > digits_sums[digits_sum][0]:
            digits_sums[digits_sum].append(number)

        else:
            digits_sums[digits_sum].insert(0, number)

        pair_sum = sum(digits_sums[digits_sum])
        if pair_sum > max_pair_sum:
            max_pair_sum = pair_sum

    return max_pair_sum
