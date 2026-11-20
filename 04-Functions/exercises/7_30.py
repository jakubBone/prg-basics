# A program with a recursive function that sums the natural numbers from 1 to n.


def sum_natural(n):
    # the base case: the sum of numbers from 1 to 1 is 1
    if n == 1:
        return 1
    # the sum from 1 to n is n plus the sum from 1 to n - 1
    return n + sum_natural(n - 1)


print('The sum of natural numbers in the range <1,10> is', sum_natural(10))  # 55
