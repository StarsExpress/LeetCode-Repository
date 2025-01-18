
def calculate(string: str) -> int:  # LeetCode Q.224.
    string = string.replace(" ", "")  # Rip away all spaces.

    # Stack for unpaired left parentheses. Track if parenthesis has - sign at left.
    isolate_indices: list[list[int | bool]] = []  # Format: [idx, negative].
    numbers: list[list[int]] = []  # Format: [idx, number].

    for idx, char in enumerate(string):
        if char == ")":
            pair_idx, negative = isolate_indices.pop(-1)

            number = 0
            while numbers and pair_idx < numbers[-1][0] < idx:  # Num in the paired parenthesis.
                number += numbers.pop(-1)[1]

            if negative:
                number -= 2 * number
            numbers.append([idx, number])

        negative = True if string[idx - 1] == "-" else False
        if char == "(":
            isolate_indices.append([idx, negative])

        if char.isdigit():
            if numbers and numbers[-1][0] + 1 == idx:  # Last idx is also a number.
                numbers[-1][0] += 1  # Merge current digit into this number.
                numbers[-1][1] *= 10

            else:
                numbers.append([idx, 0])

            if numbers[-1][1] < 0 or negative:  # Last number or current digit is negative.
                numbers[-1][1] -= int(char)

            else:
                numbers[-1][1] += int(char)

    result = 0
    while numbers:
        result += numbers.pop(-1)[1]
    return result
