
def find_nth_digit(n: int):  # LeetCode Q.400.
    digits2counts, table_len = [], 0

    min_num, max_num = 1, n
    while True:
        mid_num = (min_num + max_num) // 2
        mid_num_len = len(str(mid_num))
        count = mid_num_len * (mid_num + 1 - 10 ** (mid_num_len - 1))

        for i in range(1, mid_num_len):
            if i > table_len:
                digits2counts.append(
                    i * 9 * (10 ** (i - 1))
                )
                table_len += 1

            count += digits2counts[i - 1]

        if count == n:
            return mid_num % 10

        if count < n:
            min_num = mid_num + 1

        else:
            max_num = mid_num - 1

        if min_num > max_num:
            return int(str(mid_num)[n - count - 1])
