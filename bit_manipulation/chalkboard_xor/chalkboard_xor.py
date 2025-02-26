
def determine_winner(numbers: list[int]) -> bool:  # LeetCode Q.810.
    xor_value = 0
    numbers2counts, distinct_numbers = dict(), []
    for number in numbers:
        xor_value ^= number
        if number not in numbers2counts.keys():
            distinct_numbers.append(number)
            numbers2counts.update({number: 0})
        numbers2counts[number] += 1

    total_finished_plays = 0  # When total plays are even, it's Alice's turn.
    removed_idx = 0
    while distinct_numbers:
        if xor_value == 0:
            return True if total_finished_plays % 2 == 0 else False

        removed_idx -= removed_idx  # Reset to the default 0.
        if distinct_numbers[0] == xor_value and len(distinct_numbers) > 1:
            removed_idx += 1  # Must and can switch to another removal choice.

        removed_num = distinct_numbers[removed_idx]
        numbers2counts[removed_num] -= 1
        if numbers2counts[removed_num] == 0:
            distinct_numbers.pop(removed_idx)

        xor_value ^= removed_num
        total_finished_plays += 1

    return True if total_finished_plays % 2 == 0 else False
