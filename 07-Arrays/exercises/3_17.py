# A program that prints a tuple in reverse order.

numbers = (10, 20, 30, 40, 50)

text = ''
for value in numbers:
    text = text + str(value) + ','
print('Tuple:', text[0:len(text) - 1])

# a tuple is indexed like a list, so it can be read from the last index to 0
reverse_text = ''
for i in range(len(numbers) - 1, -1, -1):
    reverse_text = reverse_text + str(numbers[i]) + ','
print('Reverse order:', reverse_text[0:len(reverse_text) - 1])
