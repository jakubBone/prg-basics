# A program that prints the values of a two dimensional array of size 2 by 4 in rows and columns.

arr = [
    [4, 8, 15, 16],
    [23, 42, 7, 1]
]

for row in arr:
    for value in row:
        print(value, end=' ')
    print()
