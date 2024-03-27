
def find_longest_distinction(string: str):
    if len(string) <= 0:
        return 0
    if len(set(string)) == 1:
        return 1

    # 1st char is already a substring, so iteration starts from 2nd char.
    # Track current substring's chars and their respective indices of "input string".
    chars_list, idx_list = [string[0]], [0]  # The same index means a char and its idx.

    current_len, max_len = 1, 1  # Current substring has 1st char, so length is 1.
    current_idx, locator_idx = 1, 0  # Locator index helps update lists of substring chars and idx.

    while True:
        if current_idx >= len(string):  # Reach the end of input string.
            return max(current_len, max_len)

        if string[current_idx] not in chars_list:  # Current char isn't in current substring.
            chars_list.append(string[current_idx])
            idx_list.append(current_idx)
            current_len += 1

        else:  # Current char is already in "somewhere" of current substring.
            max_len += max(current_len - max_len, 0)  # Update max length.

            # Locate where this current char is in chars & idx list.
            locator_idx += chars_list.index(string[current_idx]) - locator_idx
            # Ensure uniqueness in current substring, and adjust its length.
            current_len += len(string[idx_list[locator_idx] + 1: current_idx + 1]) - current_len

            chars_list = chars_list[locator_idx + 1:]  # Update chars and idx list.
            chars_list.append(string[current_idx])
            idx_list = idx_list[locator_idx + 1:]
            idx_list.append(current_idx)

        current_idx += 1  # Go to next char of input string.


if __name__ == '__main__':
    print(find_longest_distinction('abcabcbb'))
