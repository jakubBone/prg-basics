# A program with a function that returns a transposed matrix (rows become columns and columns become rows).


def transpose_matrix(m):
    rows = len(m)
    columns = len(m[0])
    # the transposed matrix has as many rows as m has columns
    result = [[0 for j in range(rows)] for i in range(columns)]
    for i in range(rows):
        for j in range(columns):
            result[j][i] = m[i][j]
    return result


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()


matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]]
]

for matrix in matrices:
    print('Matrix:')
    print_matrix(matrix)
    print('Transposed matrix:')
    print_matrix(transpose_matrix(matrix))
    print()
