# A program that reads an amount from the keyboard
# and prints it with its 23% VAT, both with two decimal places.

amount = float(input('Enter an amount: '))

tax_in_percent = 0.23
tax_to_pay = amount * tax_in_percent

print(f'Amount: {amount:.2f}')
print(f'Tax to pay: {tax_to_pay:.2f}')
