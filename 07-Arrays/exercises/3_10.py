# A program that prints array values graphically: each number is followed by that many asterisks.


def star(n):
    # a string multiplied by a number is repeated
    return '*' * n


arr = [2, 6, 4, 9, 7]

for value in arr:
    print(f'{value}: {star(value)}')
