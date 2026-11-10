# A program that calculates the total washing time of a washing machine.
# Jacket 40 min, underwear 70 min, shoes 20 min, additional rinse 15 min, additional spin 9 min.

washing_product = "shoes"
rinse = True
spin = False

total_time = 0

if washing_product == "jacket":
    total_time = 40
elif washing_product == "underwear":
    total_time = 70
elif washing_product == "shoes":
    total_time = 20

if rinse:
    total_time += 15
if spin:
    total_time += 9

print(f'Total washing time: {total_time} minutes')
