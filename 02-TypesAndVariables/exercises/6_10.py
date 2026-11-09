# A program that shows basic string methods on a movie title.

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters:', len(movie))

# print title in capital letters
print('Capital letters:', movie.upper())

# print title in small letters
print('Small letters:', movie.lower())

# print how many times the vowel "e" appears in the title
print('Letter e appears:', movie.count('e'), 'times')

# print where in the text is the word "Lord"
print('Word Lord starts at index:', movie.find('Lord'))

# print where in the text is the word "dragon" (-1 means not found)
print('Word dragon starts at index:', movie.find('dragon'))
