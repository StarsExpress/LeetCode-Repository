
def replace_integer(integer: int):  # LeetCode Q.397.
    # Return number of operations to make integer 1.
    # If integer is odd: plus or minus 1; if it's even: replace it with its 50%.
    operations = 0
    while integer != 1:
        operations += 1
        if integer % 2 == 0:
            integer /= 2
            continue

        # Plus 1 whenever integer isn't 3 and plus 1 becomes 4's multiple.
        if ((integer + 1) % 4 == 0) & (integer != 3):
            integer += 1
            continue
        integer -= 1

    return operations
