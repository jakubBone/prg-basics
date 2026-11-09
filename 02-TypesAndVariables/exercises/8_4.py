# A program that prints a height both in cm and in feet and inches.

height_in_cm = 170

# 1 inch = 2.54 cm
# the number of whole inches is rounded
total_inches = round(height_in_cm / 2.54)

# 1 foot = 12 inches
height_in_feet = total_inches // 12
height_in_inches = total_inches % 12

print(f'I am {height_in_cm}cm tall, i.e. {height_in_feet} feet and {height_in_inches} inches')
