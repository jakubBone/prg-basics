# A program that checks a payment card PIN code. The user has up to three attempts,
# after three unsuccessful attempts the card is blocked.

# the PIN is kept as text, because a number would lose the leading zero (0805)
pin = '0805'
attempts = 0
pin_ok = False

while attempts < 3 and not pin_ok:
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == pin:
        pin_ok = True
        print('PIN code is correct')
    else:
        attempts += 1
        print('Incorrect...')

if not pin_ok:
    print('Sorry, your payment card has been blocked.')
