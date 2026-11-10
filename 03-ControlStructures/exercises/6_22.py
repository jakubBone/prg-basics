# A program that prints numbers from 1 to 30. Numbers divisible by 3 are replaced by THREE,
# numbers divisible by 5 by FIVE and numbers divisible by both 3 and 5 by BINGO.

for i in range(1, 31):
    # BINGO must be checked first, because a number divisible by 15 is also divisible by 3 and by 5
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')
    elif i % 3 == 0:
        print('THREE', end=' ')
    elif i % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(i, end=' ')

# end=' ' keeps everything in one line, print() finishes the line
print()
