# A program that determines where the point P(x, y) is located in the coordinate system:
# in which quadrant, on which axis, or in the origin (0,0).

x = int(input('x = '))
y = int(input('y = '))

if x == 0 and y == 0:
    print(f'Point P({x},{y}) is in the origin of the coordinate system')
elif x == 0:
    print(f'Point P({x},{y}) is on the y axis')
elif y == 0:
    print(f'Point P({x},{y}) is on the x axis')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
else:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
