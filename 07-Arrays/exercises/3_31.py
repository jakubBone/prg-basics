# A program with a function that creates a two dimensional array filled with zeros.


def create_2d_arr(x, y):
    # x rows, y columns; every row is a separate list
    return [[0 for j in range(y)] for i in range(x)]


arr = create_2d_arr(3, 5)

for row in arr:
    print(row)
