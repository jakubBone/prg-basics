# A program that prints a 9-digit phone number as three groups of 3 digits separated by a dash.

phone = input('Enter phone number: ')

print(f'Phone number: {phone[0:3]}-{phone[3:6]}-{phone[6:9]}')
