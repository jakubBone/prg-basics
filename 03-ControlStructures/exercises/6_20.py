# A program that converts a decimal number into a binary number by dividing by 2 and collecting the remainders.

number = int(input('Enter decimal number: '))

quotient = number
binary = ''

# every remainder is added at the BEGINNING of the text, because the last remainder is the first digit
while quotient > 0:
    remainder = quotient % 2
    binary = str(remainder) + binary
    quotient = quotient // 2

# for 0 the loop does not run at all
if number == 0:
    binary = '0'

print(f'{number}(10) = {binary}(2)')
