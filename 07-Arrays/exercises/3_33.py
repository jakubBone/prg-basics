# A program that finds the smallest and the largest value in a two dimensional array and their positions.

arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value = arr[0][0]
min_row = 0
min_column = 0
max_value = arr[0][0]
max_row = 0
max_column = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min_value:
            min_value = arr[i][j]
            min_row = i
            min_column = j
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_row = i
            max_column = j

# +1, because rows and columns are counted from 1 for people (the indexes start from 0)
print(f'Smallest value: {min_value} (row {min_row + 1}, column {min_column + 1})')
print(f'Largest value: {max_value} (row {max_row + 1}, column {max_column + 1})')
