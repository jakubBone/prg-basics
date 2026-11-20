# A program that swaps the first and the last row of a two dimensional array of size 3 by 5.

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

# the rows are lists, so swapping them needs a temporary variable
last = len(arr) - 1
temp = arr[0]
arr[0] = arr[last]
arr[last] = temp

print('After:')
print_array(arr)
