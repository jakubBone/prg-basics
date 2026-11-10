# A program that analyses the price of a product and recommends buying it
# when the price decreased by at least 10%.

current_price = 140.00
previous_price = 200.00

print(f'Current product price: {current_price:.2f}')
print(f'Previous product price: {previous_price:.2f}')

# the percentage of the decrease relative to the previous price
reduction_percent = (previous_price - current_price) / previous_price * 100

if reduction_percent >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {reduction_percent:.0f}%')
