# A program that calculates the factorial recursively.
# (the function from the task had the second "if" outside of the function, here it is fixed)


def factorial(n):
    # 0! = 1, 1! = 1: the base case that stops the recursion
    if n == 0 or n == 1:
        return 1
    # n! = n * (n-1)!: the function calls itself with a smaller number
    return n * factorial(n - 1)


print('5! =', factorial(5))  # 120
