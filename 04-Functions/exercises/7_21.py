# A program with a function that returns the difference between the largest and the smallest of three numbers.


def difference(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)


if __name__ == "__main__":
    print('f(7,4,9) returns', difference(7, 4, 9))  # 5
    print('f(2,12,8) returns', difference(2, 12, 8))  # 10
