# A program that checks whether the first array is a subset of the second one
# (all elements of the first array appear in the second array).

first = [2, 5, 7]
second = [1, 2, 3, 5, 7, 9]

is_subset = True
for element in first:
    if element not in second:
        is_subset = False
        break

print('First array:', first)
print('Second array:', second)
if is_subset:
    print('The first array is a subset of the second one')
else:
    print('The first array is not a subset of the second one')
