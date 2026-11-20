# A program that fills a 5x5 array with a multiplication table and prints it.

arr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# the value in the row i and the column j is (i + 1) * (j + 1), because the indexes start from 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = (i + 1) * (j + 1)

for row in arr:
    for value in row:
        print(f'{value:3d}', end='')
    print()
