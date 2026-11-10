# A program that acts as a payment terminal: it checks whether the account balance covers the purchases.

account_balance = 500
total_payment = int(input('Enter total payment: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')
