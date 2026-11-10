# A program that calculates the sum of integer numbers in the range <5,10>.

total = 0

# range(5, 11) gives 5, 6, ..., 10 (the end 11 is not included)
for i in range(5, 11):
    total += i  

print(f'Sum is {total}')
