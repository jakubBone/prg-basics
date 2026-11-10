# A program that prints a computer numeric keyboard using while loops instead of for loops.
#
# 7 8 9
# 4 5 6
# 1 2 3

# i is the number before the first key of a row: 6, 3, 0 (rows 7 8 9, 4 5 6, 1 2 3)
i = 6
while i >= 0:
    # j goes through the three keys of a row, the key is i + j
    j = 1
    while j <= 3:
        print(f'{i+j}', end=' ')
        j += 1
    print()  # new line after each row
    i -= 3
