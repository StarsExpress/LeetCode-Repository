
def count_possibilities(record_len: int) -> int:  # LeetCode Q.552.
    modulo = 10 ** 9 + 7

    # Possible suffixes: "a", "p", "l", "ll".
    one_absence_table = {"a": 1, "p": 0, "l": 0, "ll": 0}  # Base case: record len = 1.

    # Possible suffixes: "p", "l", "ll".
    no_absence_table = {"p": 1, "l": 1, "ll": 0}  # Base case: record len = 1.

    # Help each day's tables update values.
    new_one_absence_table, new_no_absence_table = dict(), dict()

    for _ in range(2, record_len + 1):
        # Update counts of those w/ 1 absence and suffix "a".
        new_one_absence_table["a"] = sum(no_absence_table.values()) % modulo

        # Update counts of those w/ 1 absence and suffix "p".
        new_one_absence_table["p"] = sum(one_absence_table.values()) % modulo

        # Update counts of those w/ 1 absence and suffix "l".
        new_one_absence_table["l"] = one_absence_table["a"] + one_absence_table["p"]

        # Update counts of those w/ 1 absence and suffix "ll".
        new_one_absence_table["ll"] = one_absence_table["l"]

        # Update counts of those w/o absence and has suffix "l" or "ll".
        new_no_absence_table["l"] = no_absence_table["p"]
        new_no_absence_table["ll"] = no_absence_table["l"]

        # Update counts of those w/o absence and has suffix "p".
        new_no_absence_table["p"] = sum(no_absence_table.values()) % modulo

        one_absence_table.update(new_one_absence_table)
        no_absence_table.update(new_no_absence_table)

        new_one_absence_table.clear()  # Reset for next day's usage.
        new_no_absence_table.clear()

    valid_combinations = sum(one_absence_table.values()) + sum(no_absence_table.values())
    valid_combinations %= modulo
    return valid_combinations
