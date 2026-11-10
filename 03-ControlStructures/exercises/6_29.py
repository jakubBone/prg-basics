# A program that finds the first N prime numbers (N is read from the keyboard).
# A prime number is divisible only by 1 and by itself.

n = int(input('Enter N: '))

found = 0
candidate = 2

while found < n:
    is_prime = True
    # check every number from 2 to candidate - 1; if any divides the candidate, it is not prime
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(candidate, end=' ')
        found += 1
    candidate += 1

print()
