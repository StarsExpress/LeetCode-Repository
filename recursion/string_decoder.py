
digits = [str(i) for i in range(10)]


def decode_string(string: str, recursive: bool = False) -> str:  # LeetCode Q.394.
    if len(string) <= 1:
        return string

    # Decode everything at 1st char's right side.
    decoded_right = decode_string(string[1:], recursive=True)
    head = string[0]  # 1st char.
    if head in digits:  # Head is digit.
        if recursive:  # Input string is from "recursive call".
            return f"{head}{decoded_right}"

        bracket_end, decoded_digit = decoded_right.index("]"), ""
        for s in decoded_right:  # Collect until no more digits.
            if s not in digits:
                break
            decoded_digit += s

        multiple = int(f'{head}{decoded_digit}')  # Head is also digit.
        # Decoded digit's length = index of "[".
        # Multiple works inside ("exclusive of") brackets.
        decoded_bracket = decoded_right[len(decoded_digit) + 1: bracket_end] * multiple

        decoded_bracket += decoded_right[bracket_end + 1:]
        return decoded_bracket

    if decoded_right[0] in digits:  # If right side starts with digit.
        bracket_end, decoded_digit = decoded_right.index("]"), ""
        for s in decoded_right:
            if s not in digits:
                break
            decoded_digit += s

        multiple = int(decoded_digit)  # Head isn't digit.
        # Decoded digit's length = index of '['.
        # Multiple works inside ("exclusive of") brackets.
        decoded_bracket = decoded_right[len(decoded_digit) + 1: bracket_end] * multiple

        decoded_bracket += decoded_right[bracket_end + 1:]
        return f"{head}{decoded_bracket}"

    return f"{head}{decoded_right}"
