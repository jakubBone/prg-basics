# A program that checks whether a number is in the range <2,15> (the function is in the ranges module).

import ranges

number = int(input('A number: '))
low = 2
high = 15

if ranges.in_range(number, low, high):
    answer = 'yes'
else:
    answer = 'no'

print(f'Number {number} in the range <{low},{high}>: {answer}')
