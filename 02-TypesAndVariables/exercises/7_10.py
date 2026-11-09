# A program in which a user tries to guess the number rolled by the computer.

import random

# COMPUTER TURN
computer = random.randint(1, 6)

# YOUR TURN
# input() returns a string, so it must be converted to int before comparing
you = int(input('Guess the number (1-6): '))

print(f'You won: {you == computer}')
print(f'Computer number is: {computer}')
