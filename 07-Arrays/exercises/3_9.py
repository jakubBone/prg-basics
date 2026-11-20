# A program that prints the longest name (the largest number of characters) from an array of names.

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = names[0]
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print('Names:', end=' ')
for name in names:
    print(name, end=' ')
print()
print('Longest name:', longest_name)
