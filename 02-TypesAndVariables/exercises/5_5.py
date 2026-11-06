# A program that reads a product price and a discount in percent
# and prints the price with the discount and the reduction, both with two decimal places.

price = float(input('Enter price: '))
discount = float(input('Enter discount in %: '))

price_with_discount = price * (1 - discount / 100)
reduction = price - price_with_discount

print(f'Price with discount: {price_with_discount:.2f}')
print(f'Reduction: {reduction:.2f}')
