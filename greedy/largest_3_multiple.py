
def find_largest_3_multiple(digits: list[int]) -> str:  # LeetCode Q.1363.
    digits_0369_table, digits_258_table = dict(), dict()
    digits_147_table, digits_sum = dict(), 0

    for digit in digits:
        digits_sum += digit
        if digit in {0, 3, 6, 9}:
            if digit not in digits_0369_table.keys():
                digits_0369_table.update({digit: 0})
            digits_0369_table[digit] += 1

        if digit in {2, 5, 8}:
            if digit not in digits_258_table.keys():
                digits_258_table.update({digit: 0})
            digits_258_table[digit] += 1

        if digit in {1, 4, 7}:
            if digit not in digits_147_table.keys():
                digits_147_table.update({digit: 0})
            digits_147_table[digit] += 1

    sum_modulo = digits_sum % 3
    while sum_modulo != 0:
        if sum_modulo == 1 and sum(digits_147_table.values()) == 0:
            sum_modulo = 2  # If 1 isn't available, replace with 2.

        if sum_modulo == 2 and sum(digits_258_table.values()) == 0:
            sum_modulo = 1  # If 2 isn't available, replace with 1.

        if sum_modulo == 1:
            for digit in (1, 4, 7):
                if digit in digits_147_table.keys():
                    digits_sum -= digit
                    sum_modulo = digits_sum % 3

                    digits_147_table[digit] -= 1
                    if digits_147_table[digit] == 0:
                        del digits_147_table[digit]

                    break  # Break for loop once found.

            continue

        for digit in (2, 5, 8):
            if digit in digits_258_table.keys():
                digits_sum -= digit
                sum_modulo = digits_sum % 3

                digits_258_table[digit] -= 1
                if digits_258_table[digit] == 0:
                    del digits_258_table[digit]

                break  # Break for loop once found.

    largest_3_multiple = ""
    for digit in range(9, -1, -1):
        modulo = digit % 3

        if modulo == 0:
            if digit in digits_0369_table.keys():
                if largest_3_multiple == "" and digit == 0:  # Case: leading zeros.
                    return "0"
                largest_3_multiple += str(digit) * digits_0369_table[digit]

        if modulo == 2:
            if digit in digits_258_table.keys():
                largest_3_multiple += str(digit) * digits_258_table[digit]

        if modulo == 1:
            if digit in digits_147_table.keys():
                largest_3_multiple += str(digit) * digits_147_table[digit]

    return largest_3_multiple
