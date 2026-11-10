# A program that checks whether an EAN-13 number has exactly 13 digits
# and whether the article was manufactured in Poland (the number starts with 590).

ean = input('Enter EAN-13 article number: ')

# isdigit() returns True if all characters of the string are digits
if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')
    if ean[0:3] == '590':
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')
