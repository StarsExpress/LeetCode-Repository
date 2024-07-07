
def multiply_big_int(int_1: int, int_2: int):
    """
    Karatsuba multiplication: int_1 = ab, int_2 = cd; int_1*int_2 = part_1 + part_2 + part_3.

    part_1 = (a*c)*10^n. part_2 = (b*c + a*d)*10^(0.5n). part_3 = b*d.
    n is the smaller digit length of two integers.
    """
    smaller_digit_len = min(len(str(int_1)), len(str(int_2)))
    if smaller_digit_len == 1:  # Check if both integers are single digits.
        return int_1 * int_2

    smaller_digit_len //= 2  # Now this variable denotes 0.5n.

    component_a = int(str(int_1)[:-smaller_digit_len])
    component_b = int(str(int_1)[-smaller_digit_len:])
    component_c = int(str(int_2)[:-smaller_digit_len])
    component_d = int(str(int_2)[-smaller_digit_len:])

    # Use (a + b)*(c + d) - a*c - b*d to get b*c + a*d.
    abcd_product = multiply_big_int(component_a + component_b, component_c + component_d)
    ac_product = multiply_big_int(component_a, component_c)
    bd_product = multiply_big_int(component_b, component_d)

    final_product = ac_product * 10 ** (2 * smaller_digit_len)
    final_product += (abcd_product - ac_product - bd_product) * 10**smaller_digit_len
    final_product += bd_product
    return final_product


if __name__ == "__main__":
    integer_1 = 3141592653589793238462643383279502884197169399375105820974944592
    integer_2 = 2718281828459045235360287471352662497757247093699959574966967627
    product = multiply_big_int(integer_1, integer_2)
    assert product == integer_1 * integer_2
    print(product)
