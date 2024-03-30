
def check_palindrome(x: int):
    x = str(x)
    return True if x[::-1] == x else False


if __name__ == '__main__':
    print(check_palindrome(-11))
