# A program that masks some digits of a credit card number (the function is in the cards module).

import cards

card_number = "5290312400019022"
print('Card number:', card_number)
print('Hidden card number:', cards.hide(card_number))
