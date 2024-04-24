
def roman_to_int(string: str):  # LeetCode Q.13.
    integer, add_v, add_l, add_d = 0, True, True, True
    digits_list = []

    digits_list.extend([idx for idx, char in enumerate(string) if char == 'I'])
    for i_digit in digits_list:  # Iterate through all I.
        if i_digit + 1 < len(string):
            if string[i_digit + 1] == 'V':
                integer += 4
                add_v = False
                continue

            if string[i_digit + 1] == 'X':
                integer += 9
                continue

        integer += 1

    digits_list.clear()
    digits_list.extend([idx for idx, char in enumerate(string) if char == 'X'])
    for x_digit in digits_list:   # Iterate through all X.
        if x_digit + 1 < len(string):
            if string[x_digit + 1] == 'L':
                integer += 40
                add_l = False
                continue

            if string[x_digit + 1] == 'C':
                integer += 90
                continue

        if x_digit > 0:
            if string[x_digit - 1] == 'I':
                continue

        integer += 10

    digits_list.clear()
    digits_list.extend([idx for idx, char in enumerate(string) if char == 'C'])
    for c_digit in digits_list:  # Iterate through all C.
        if c_digit + 1 < len(string):
            if string[c_digit + 1] == 'D':
                integer += 400
                add_d = False
                continue

            if string[c_digit + 1] == 'M':
                integer += 900
                continue

        if c_digit > 0:
            if string[c_digit - 1] == 'X':
                continue

        integer += 100

    digits_list.clear()
    digits_list.extend([idx for idx, char in enumerate(string) if char == 'M'])
    for m_digit in digits_list:  # Iterate through all M.:
        if m_digit > 0:
            if string[m_digit - 1] == 'C':
                continue

        integer += 1000

    if ('V' in string) & add_v:
        integer += 5
    if ('L' in string) & add_l:
        integer += 50
    if ('D' in string) & add_d:
        integer += 500
    return integer
