
def check_palindrome(x: int):
    x = str(x)
    return True if x[::-1] == x else False
