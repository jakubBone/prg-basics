# A program with a function that returns the n-th value of the Fibonacci sequence (0, 1, 1, 2, 3, 5, ...).


def fibonacci(n):
    previous = 0
    current = 1
    # after each step previous is the next value of the sequence
    for i in range(n - 1):
        next_value = previous + current
        previous = current
        current = next_value
    return previous


if __name__ == "__main__":
    print('f(5) returns', fibonacci(5))  # 3
    print('f(9) returns', fibonacci(9))  # 21
