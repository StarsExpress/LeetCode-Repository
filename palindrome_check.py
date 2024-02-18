
def check_palindrome(x:int) -> bool:
    x = str(x)
    if x[::-1] == x:
        return True
    return False


if __name__ == '__main__':
    print(check_palindrome(-11))
