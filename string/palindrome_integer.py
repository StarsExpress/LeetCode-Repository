
def check_palindrome(integer: int):  # LeetCode Q.9.
    integer = str(integer)
    return integer[::-1] == integer
