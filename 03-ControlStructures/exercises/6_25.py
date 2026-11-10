# A program that prints a pattern of digits: the digit n is repeated n times in row n.

for i in range(1, 10):
    # str(i) turns the number into text, which can be repeated i times
    print(str(i) * i)
