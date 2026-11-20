# A module with a function that masks a credit card number.

def hide(card_number):
    # the first two and the last four digits stay visible, the digits in the middle are replaced with *
    middle_length = len(card_number) - 6
    return card_number[0:2] + '*' * middle_length + card_number[-4:]
