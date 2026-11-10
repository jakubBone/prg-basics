# A program that prints a lottery coupon (numbers from 1 to 49) in 7 rows and 7 columns.

# row 1 is 1 8 15 ..., row 2 is 2 9 16 ...: the number is row + column * 7
for row in range(1, 8):
    for column in range(7):
        print(row + column * 7, end=' ')
    print()
