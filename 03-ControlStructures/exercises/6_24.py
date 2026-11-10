# A program that prints a pattern of stars: 1 to 5 stars in a row, then back from 4 to 1.

# a string multiplied by a number is repeated: '* ' * 3 is '* * * '
for i in range(1, 6):
    print('* ' * i)

# range(4, 0, -1) counts down: 4, 3, 2, 1
for i in range(4, 0, -1):
    print('* ' * i)
