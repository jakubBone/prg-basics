# A simple calculator: it reads two numbers and an operation symbol (+, -, *, /) and prints the result.

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
operator = input('Enter operation (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    # / always returns a float, e.g. 6 / 3 is 2.0
    result = number1 / number2
else:
    result = 'incorrect operation symbol'

# print result
print(f'{number1} {operator} {number2} = {result}')
