# A program that calculates the area and circumference of a circle.

# determine radius and PI values
radius = float(input('Enter radius: '))

# math.pi could be used instead (more precise), but 3.14 matches the task examples:
# r = 1 --> circumference = 6.28, area = 3.14
# r = 3 --> circumference = 18.84, area = 28.26
pi = 3.14

# calculate area
area = pi * radius ** 2

# calculate circumference
circumference = 2 * pi * radius

# print results
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')
