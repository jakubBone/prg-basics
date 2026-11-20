# A program that separates even and odd numbers of an array: first all even numbers, then all odd numbers.

arr = [7, 9, 2, 4, 5, 6]
print('arr =', arr)

evens = []
odds = []
for number in arr:
    if number % 2 == 0:
        evens.append(number)  # append() adds an element at the end of the list
    else:
        odds.append(number)

# + joins two lists
arr = evens + odds
print('arr =', arr)
