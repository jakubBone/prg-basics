# A program that rolls a die and checks whether the number is special (1 or 6).

import random

dice = random.randint(1, 6)
special = dice == 1 or dice == 6

print(f'Dice rolled: {dice}')
print(f'Special number (1 or 6): {special}')
