# A program with a function that returns the n-th prime number.


def nth_prime(n):
    found = 0
    candidate = 1
    while found < n:
        candidate += 1
        is_prime = True
        # a prime number is not divisible by any number from 2 to candidate - 1
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            found += 1
    return candidate


if __name__ == "__main__":
    print('f(1) returns', nth_prime(1))  # 2
    print('f(5) returns', nth_prime(5))  # 11
