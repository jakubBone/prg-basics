# A program that prints the first twenty terms of the Fibonacci sequence.
# The first term is 0, the second is 1, each next term is the sum of the previous two.

previous = 0
current = 1

for i in range(20):
    print(previous, end=' ')
    next_term = previous + current
    previous = current
    current = next_term

print()
