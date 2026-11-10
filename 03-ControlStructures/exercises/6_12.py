# A program that calculates the amount to pay when a 25% discount is charged
# for each product purchased over two.

number_of_products = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if number_of_products <= 2:
    amount_to_pay = number_of_products * price
else:
    # the first two products at full price, the rest at 75% of the price
    amount_to_pay = 2 * price + (number_of_products - 2) * price * 0.75

print(f'Amount to pay: {amount_to_pay:.2f}')
