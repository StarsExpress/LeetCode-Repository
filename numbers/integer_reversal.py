
def reverse_integer(x: int) -> int:
    output_list = []
    for s in str(x).replace('-', ''):
        output_list.append(s)

    output = int(''.join(list(reversed(output_list))))

    if (output < -(2 ** 31)) | (output > 2 ** 31):
        return 0

    if x < 0:
        return 0 - output
    return output


if __name__ == '__main__':
    print(reverse_integer(15342364))
