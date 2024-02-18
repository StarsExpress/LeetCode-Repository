
def roman_to_int(s: str) -> int:
    value, add_v, add_l, add_d = 0, True, True, True
    list_temp = []

    list_temp.extend([n for (n, e) in enumerate(s) if e == 'I'])
    for i in list_temp:  # Iterate through all I.
        if i + 1 < len(s):
            if s[i + 1] == 'V':
                value += 4
                add_v = False
                continue
            if s[i + 1] == 'X':
                value += 9
                continue
        value += 1

    list_temp.clear()
    list_temp.extend([n for (n, e) in enumerate(s) if e == 'X'])
    for x in list_temp:   # Iterate through all X.
        if x + 1 < len(s):
            if s[x + 1] == 'L':
                value += 40
                add_l = False
                continue
            if s[x + 1] == 'C':
                value += 90
                continue
        if x > 0:
            if s[x - 1] == 'I':
                continue
        value += 10

    list_temp.clear()
    list_temp.extend([n for (n, e) in enumerate(s) if e == 'C'])
    for c in list_temp:  # Iterate through all C.
        if c + 1 < len(s):
            if s[c + 1] == 'D':
                value += 400
                add_d = False
                continue
            if s[c + 1] == 'M':
                value += 900
                continue
        if c > 0:
            if s[c - 1] == 'X':
                continue
        value += 100

    list_temp.clear()
    list_temp.extend([n for (n, e) in enumerate(s) if e == 'M'])
    for m in list_temp:  # Iterate through all M.:
        if m > 0:
            if s[m - 1] == 'C':
                continue
        value += 1000

    if ('V' in s) & add_v:
        value += 5
    if ('L' in s) & add_l:
        value += 50
    if ('D' in s) & add_d:
        value += 500
    return value


if __name__ == '__main__':
    print(roman_to_int('MMMCMXCIV'))
