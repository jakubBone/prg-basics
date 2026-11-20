# A program that calculates the sum of the digits in a number using a function.


def sum_digits(number):
    # abs() removes the minus sign, str() makes it possible to go through the digits one by one
    digits = str(abs(number))
    total = 0
    for digit in digits:
        total += int(digit)  # int() turns the character back into a number
    return total


any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
