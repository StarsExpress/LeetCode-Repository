
def find_largest_3_multiple(digits: list[int]) -> str:  # LeetCode Q.1363.
    digits.sort(reverse=True)
    digits_sum, mods2indices = 0, dict()
    for idx, digit in enumerate(digits):
        digits_sum += digit
        modulo = digit % 3
        if modulo != 0:  # Only consider mod 1 and 2.
            if modulo not in mods2indices.keys():
                mods2indices.update({modulo: []})
            mods2indices[modulo].append(idx)

    sum_modulo, skipped_indices = digits_sum % 3, set()
    while sum_modulo != 0:
        if sum_modulo not in mods2indices.keys():  # Mod must be either 1 or 2.
            sum_modulo = 1 if sum_modulo == 2 else 2

        digits_sum -= digits[mods2indices[sum_modulo][-1]]  # Remove smaller digit.
        skipped_indices.add(mods2indices[sum_modulo].pop(-1))
        sum_modulo = digits_sum % 3

    largest_3_multiple = ""
    for idx, digit in enumerate(digits):
        if idx not in skipped_indices:
            if largest_3_multiple == "" and digit == 0:  # Base case.
                return "0"
            largest_3_multiple += str(digit)

    return largest_3_multiple
