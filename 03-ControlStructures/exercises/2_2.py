# A program that prints a verbal description of a clothing size symbol (S, M, L, XL).

size = input('Enter size symbol: ')

# elif checks the next condition only if all the previous ones were False
# else is executed when none of the conditions is True
if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')
