# A program that swaps the first and the last column of a two dimensional array of size 3 by 5.

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]


def print_array(arr):
    for row in arr:
        for value in row:
            print(f'{value:3d}', end='')
        print()


print('Before:')
print_array(arr)

# in every row the first and the last element are swapped
for row in arr:
    last = len(row) - 1
    temp = row[0]
    row[0] = row[last]
    row[last] = temp

print('After:')
print_array(arr)
