# A program that replaces the values of the main diagonal of a square matrix with 1.

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# the main diagonal consists of the elements with equal row and column indexes
for i in range(len(matrix)):
    matrix[i][i] = 1

for row in matrix:
    for value in row:
        print(value, end=' ')
    print()
