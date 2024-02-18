
def multiply_big_int(int_1, int_2):
    smaller_digit_len = min(len(str(int_1)), len(str(int_2)))  # Check if both integers are single digits.
    if smaller_digit_len == 1:
        return int_1 * int_2

    # Karatsuba multiplication: int_1 = ab, int_2 = cd; int_1*int_2 = part_1 + part_2 + part_3.
    # part_1 = (a*c)*10^n. part_2 = (b*c + a*d)*10^(0.5n). part_3 = b*d.
    # n is the smaller digit length of two integers.
    smaller_digit_len //= 2  # Now this variable denotes 0.5n.
    component_a, component_b = int(str(int_1)[:-smaller_digit_len]), int(str(int_1)[-smaller_digit_len:])
    component_c, component_d = int(str(int_2)[:-smaller_digit_len]), int(str(int_2)[-smaller_digit_len:])
    del int_1, int_2  # Reduce memory by deletion of no-longer-used variables.

    # Use (a + b)*(c + d) - a*c - b*d to get b*c + a*d.
    abcd_multiplication = multiply_big_int(component_a + component_b, component_c + component_d)
    ac_multiplication = multiply_big_int(component_a, component_c)
    bd_multiplication = multiply_big_int(component_b, component_d)
    del component_a, component_b, component_c, component_d

    final_multiplication = ac_multiplication * 10 ** (2 * smaller_digit_len)
    final_multiplication += (abcd_multiplication - ac_multiplication - bd_multiplication) * 10 ** smaller_digit_len
    final_multiplication += bd_multiplication
    del abcd_multiplication, ac_multiplication, bd_multiplication, smaller_digit_len
    return final_multiplication


if __name__ == '__main__':
    integer_1 = 3141592653589793238462643383279502884197169399375105820974944592462643383279502884793238462643385765
    integer_2 = 2718281828459045235360287471352662497757247093699959574966967627028747135266249182845904523536029821
    assert multiply_big_int(integer_1, integer_2) == integer_1 * integer_2
    print(multiply_big_int(integer_1, integer_2))
