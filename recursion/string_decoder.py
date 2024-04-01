
str_to_digit = dict(zip([str(i) for i in range(10)], [i for i in range(10)]))


def decode_string(string: str):  # LeetCode Q.394.
    if len(string) <= 1:
        return string

    head = string[0]
    if head in str_to_digit.keys():
        decoded_str = decode_string(string[1:])
        if '[' in decoded_str:
            left_idx, right_idx = decoded_str.index('['), decoded_str.index(']')
            output_str = decoded_str[:left_idx]
            output_str += decoded_str[left_idx + 1: right_idx] * str_to_digit[head]
            return f'{output_str}{decoded_str[right_idx + 1:]}'

        return f'{decoded_str * str_to_digit[head]}'

    return f'{head}{decode_string(string[1:])}'


if __name__ == '__main__':
    print(decode_string("100[leetcode]"))
