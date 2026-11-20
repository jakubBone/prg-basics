# A program that prints the name of a month based on the month number (the function is in the months module).

import months

number = int(input('Enter month number: '))
print(f'The name of month {number} is {months.month(number)}')
