# A program with a function that checks whether at least one of three numbers is negative.


def any_negative(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0


if __name__ == "__main__":
    print('f(11,6,-4) returns', any_negative(11, 6, -4))  # True
    print('f(5,4,14) returns', any_negative(5, 4, 14))  # False
