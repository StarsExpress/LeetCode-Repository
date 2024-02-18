
def int_to_roman(num: int) -> str:
    output = ''
    map_dict = dict(zip([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
                        ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']))

    for m in map_dict.keys():
        if num >= m:
            output += map_dict[m] * (num // m)
            num %= m

    return output


if __name__ == '__main__':
    print(int_to_roman(1996))
