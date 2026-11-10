# A program that shows an amount of PLN with as few coins (1, 2 and 5 PLN) as possible.

amount = int(input('Enter the amount in PLN: '))

# take as many of the biggest coins as possible, then repeat for the rest
coins_5 = amount // 5
rest = amount % 5
coins_2 = rest // 2
coins_1 = rest % 2

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')
