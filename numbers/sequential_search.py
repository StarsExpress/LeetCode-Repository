
str_1_to_9 = ''.join(str(i) for i in range(1, 10))  # 123456789 in string.


def find_sequential_digits(floor: int, ceiling: int):  # LeetCode Q.1291.
    seqs, min_len, max_len = [], len(str(floor)), len(str(ceiling))

    start_idx = 0  # The start of string slice.
    for i in range(min_len, max_len + 1):
        while True:
            if start_idx + i > len(str_1_to_9):  # When string's end is reached.
                start_idx -= start_idx  # Reset start idx to 0 for next iteration of for loop.
                break

            seq_slice = int(str_1_to_9[start_idx: start_idx + i])
            if floor <= seq_slice <= ceiling:
                seqs.append(seq_slice)
            start_idx += 1  # Increment for next iteration of while loop.

    return seqs
