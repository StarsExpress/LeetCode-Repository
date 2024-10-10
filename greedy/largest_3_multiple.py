
def find_largest_3_multiple(digits: list[int]) -> str:  # LeetCode Q.1363.
    table_0369, table_258 = dict(), dict()
    table_147, digits_sum = dict(), 0

    for digit in digits:
        digits_sum += digit
        if digit in {0, 3, 6, 9}:
            if digit not in table_0369.keys():
                table_0369.update({digit: 0})
            table_0369[digit] += 1

        if digit in {2, 5, 8}:
            if digit not in table_258.keys():
                table_258.update({digit: 0})
            table_258[digit] += 1

        if digit in {1, 4, 7}:
            if digit not in table_147.keys():
                table_147.update({digit: 0})
            table_147[digit] += 1

    sum_modulo = digits_sum % 3
    # True: seek digits of mod 1; False: seek digits of mod 1.
    mod_1_search = True if sum_modulo == 1 else False
    while sum_modulo > 0:
        if mod_1_search:
            for digit in (1, 4, 7):
                if digit in table_147.keys():
                    sum_modulo -= 1  # Mod sums 1 & 2 become 0 & 1, respectively.

                    table_147[digit] -= 1
                    if table_147[digit] == 0:
                        del table_147[digit]

                    break  # Break for loop.

            if sum_modulo == 0:
                break  # Break while loop.
            mod_1_search = False  # No digits of mod 1: seek digits of mod 2.

        if not mod_1_search:
            for digit in (2, 5, 8):
                if digit in table_258.keys():
                    if sum_modulo == 2:  # Mod sum 2: now becomes mod sum 0.
                        sum_modulo = 0
                    if sum_modulo == 1:  # Mod sum 1: now becomes mod sum 2.
                        sum_modulo = 2

                    table_258[digit] -= 1
                    if table_258[digit] == 0:
                        del table_258[digit]

                    break  # Break for loop.

            mod_1_search = True  # No digits of mod 2: seek digits of mod 1.

    if not table_147 and not table_258 and set(table_0369.keys()) == {0}:
        return "0"  # Case: leading zeros.

    largest_3_multiple = ""
    for digit in range(9, -1, -1):
        if digit in {0, 3, 6, 9}:
            if digit in table_0369.keys():
                largest_3_multiple += str(digit) * table_0369[digit]

        if digit in {2, 5, 8}:
            if digit in table_258.keys():
                largest_3_multiple += str(digit) * table_258[digit]

        if digit in {1, 4, 7}:
            if digit in table_147.keys():
                largest_3_multiple += str(digit) * table_147[digit]

    return largest_3_multiple
