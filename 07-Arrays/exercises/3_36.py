# A program with functions that create and print an identity matrix (ones on the main diagonal, zeros elsewhere).


def identity_matrix(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()


for size in (3, 5, 8):
    print(f'Identity matrix {size}x{size}:')
    print_matrix(identity_matrix(size))
    print()
