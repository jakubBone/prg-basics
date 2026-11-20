# A program with a recursive function that calculates x to the power of n.


def power(x, n):
    # the base case: any number to the power of 0 is 1
    if n == 0:
        return 1
    # x^n = x * x^(n-1)
    return x * power(x, n - 1)


print('5^3 =', power(5, 3))  # 125
