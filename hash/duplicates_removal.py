
def remove_duplicates(integers: list[int]):  # LeetCode Q.80.
    counts_table = dict()  # Required to modify integers list "in-place" without using copies.
    for integer in integers:  # Each int's count.
        if integer not in counts_table.keys():
            counts_table.update({integer: 0})

        if counts_table[integer] == 2:  # Required to set max count at 2.
            continue
        counts_table[integer] += 1

    integers.clear()
    for integer in counts_table.keys():
        integers.extend([integer] * counts_table[integer])
    return len(integers)
