# A program with a function that returns the numbers from 1 to n as one string.


def numbers_string(n):
    result = ''
    for number in range(1, n + 1):
        # str() changes the number to text, so it can be joined with +
        result = result + str(number)
    return result


if __name__ == "__main__":
    print('f(11) returns', numbers_string(11))  # 1234567891011
    print('f(4) returns', numbers_string(4))  # 1234
