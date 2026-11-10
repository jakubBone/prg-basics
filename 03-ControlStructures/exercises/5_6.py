# A program that calculates the sum of even numbers from 1 to a given number N using a while loop.

N = 10
sum_even = 0

# a while loop needs its own counter: start value, condition and the step
i = 1
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
