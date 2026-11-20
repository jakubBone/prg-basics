# A program that uses the functions of the module my_arrays (MyArrays) for a sequence of numbers.

import my_arrays

numbers = [7, 3, 8, 5, 2]

smallest_and_largest = my_arrays.min_max(numbers)

print('Numbers: 7,3,8,5,2')
print('Second largest number:', my_arrays.second_largest(numbers))
print('Difference between the largest and the smallest:', my_arrays.difference(numbers))
print('Median:', my_arrays.median(numbers))
print(f'Smallest and largest number: {smallest_and_largest[0]},{smallest_and_largest[1]}')
print('Numbers as a string:', my_arrays.to_text(numbers))
