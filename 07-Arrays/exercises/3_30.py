# A program that calculates the sum of the values in the last column of a two dimensional array.

arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0
for row in arr:
    # row[-1] (or row[len(row) - 1]) is the last element of the row
    total += row[len(row) - 1]

print('Sum of values in the last column:', total)
