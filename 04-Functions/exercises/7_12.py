# A program with a function that returns a string of n asterisks separated by a slash.


def asterisks(n):
    if n < 1:
        return ''
    # the first asterisk, then n - 1 times "/*"
    return '*' + '/*' * (n - 1)


if __name__ == "__main__":
    print('f(4) returns', asterisks(4))  # */*/*/*
    print('f(1) returns', asterisks(1))  # *
