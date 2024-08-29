
def count_max_groups(total_rows: int, reserved_seats: list[list[int]]):  # LeetCode Q.1386.
    reserved_seats.sort()
    current_row, last_col = reserved_seats[0][0], 0  # Last reserved seat's col.
    max_groups = (current_row - 1) * 2  # Deal with entire empty front rows.
    for reserved_row, reserved_col in reserved_seats:
        if reserved_row > current_row:  # Row change.
            # Clean up last reserved row's remaining cols.
            if last_col <= 5:  # Plus 2 if col is 1; otherwise, plus 1.
                max_groups += (6 - last_col) // 5 + 1

            max_groups += (reserved_row - 1 - current_row) * 2
            if 6 <= reserved_col <= 10:  # Plus 2 if col is 10; otherwise, plus 1.
                max_groups += (reserved_col - 5) // 5 + 1

            current_row, last_col = reserved_row, reserved_col
            continue

        empty_streak = reserved_col - 1 - last_col
        if empty_streak > 4:
            max_groups += 1
            if reserved_col == 10 and last_col <= 1:
                max_groups += 1

        if empty_streak == 4 and reserved_col in {6, 8, 10}:
            max_groups += 1

        last_col = reserved_col

    # Clean up last reserved row's remaining cols.
    if last_col <= 5:  # Plus 2 if col is 1; otherwise, plus 1.
        max_groups += (6 - last_col) // 5 + 1

    return max_groups + (total_rows - current_row) * 2  # Clean up entire empty remaining rows.
