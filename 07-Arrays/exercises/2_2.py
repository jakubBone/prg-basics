# A program that prints a Tic-Tac-Toe board stored in a two dimensional list.

# 3x3 Tic-Tac-Toe board: a list of rows, each row is a list of cells
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

for row in tic_tac_toe_board:
    for cell in row:
        print(cell, end=" ")
    print()
