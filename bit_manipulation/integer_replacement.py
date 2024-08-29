
def replace_integer(integer: int):  # LeetCode Q.397.
    """Return number of operations to make integer 1."""
    operations = 0
    while integer > 1:
        if integer <= 3:
            operations += integer - 1
            break

        if integer % 4 == 1:
            integer -= 1
            operations += 1

        if integer % 4 == 3:
            integer += 1
            operations += 1

        integer >>= 1
        operations += 1

    return operations
