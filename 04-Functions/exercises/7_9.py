# A program with a function that sums the even or the odd digits of a number.


def sum_digits_by_parity(number, even):
    total = 0
    for char in str(abs(number)):
        digit = int(char)
        # (digit % 2 == 0) is True for an even digit, so it is compared with the parameter even
        if (digit % 2 == 0) == even:
            total += digit
    return total


if __name__ == "__main__":
    print('f(3124,True) returns', sum_digits_by_parity(3124, True))  # 6
    print('f(3124,False) returns', sum_digits_by_parity(3124, False))  # 4
    print('f(20576,False) returns', sum_digits_by_parity(20576, False))  # 12
    print('f(20576,True) returns', sum_digits_by_parity(20576, True))  # 8
    print('f(13115,True) returns', sum_digits_by_parity(13115, True))  # 0
