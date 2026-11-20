# A program that finds which expense category was the most expensive.

categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# the two lists are parallel: the expense at index i belongs to the category at index i
max_index = 0
for i in range(len(expenses)):
    if expenses[i] > expenses[max_index]:
        max_index = i

print(f'The most expensive category: {categories[max_index]} ({expenses[max_index]})')
